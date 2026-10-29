from PIL import Image
import sys
import math
import random

class ImageDrawing:
    def __init__(self, root, img_path, pixel_size, speed, signature, character_set, program_title, background_color, tk):
        self.root = root
        self.root.title(program_title)
        self.root.configure(bg=background_color)
        
        self.pixel_size = pixel_size
        self.speed = speed
        self.signature = signature
        self.character_set = character_set

        try:
            self.img = Image.open(img_path)

            self.img.thumbnail((800, 800)) 
        except FileNotFoundError:
            print(f"Error: '{img_path}' not found.")
            sys.exit(1)
            
        self.width, self.height = self.img.size
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height + 40, bg=background_color, highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)
        
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        
        # Pikselleri merkezden dışa doğru hesapla
        self.coordinates = self.sort_the_points()
        self.current_index = 0
        
        self.root.after(500, self.advance_the_drawing)
        
        
    def sort_the_points(self):
        points = []
        
        for y in range(0, self.height, self.pixel_size):
            for x in range(0, self.width, self.pixel_size):
                distance = math.hypot(x - self.center_x, y - self.center_y)
                angle = math.atan2(y - self.center_y, x - self.center_x)
                points.append((distance, angle, x, y))
        
        points.sort(key=lambda p: (p[0], p[1]))
        return [(p[2], p[3]) for p in points]
    
    def rgb_to_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def advance_the_drawing(self):
        end_index = min(self.current_index + self.speed, len(self.coordinates))
        
        for i in range(self.current_index, end_index):
            x, y = self.coordinates[i]
            
            try:
                r, g, b = self.img.getpixel((x, y))[:3]
                hex_color = self.rgb_to_hex(r, g, b)
                character = random.choice(self.character_set)
                
                self.canvas.create_text(
                    x, y, 
                    text=character, 
                    fill=hex_color, 
                    font=("Courier", self.pixel_size, "bold") 
                )
                
                
            except IndexError:
                pass
            
        self.current_index = end_index
        if self.current_index < len(self.coordinates):
            self.root.after(5, self.advance_the_drawing)
        else:
            self.show_signature()
            
            
    def show_signature(self):
        self.canvas.create_text(
            self.center_x, self.height + 20, 
            text=self.signature, 
            fill="white", 
            font=("Courier", 12, "bold")
        )