import json
import tkinter as tk

from utils.imageDrawingClass import ImageDrawing

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, 'json', 'settings.json')

with open(SETTINGS_PATH, 'r') as f:
    settings = json.load(f)
    
    #image settings
    image_settings = settings.get("image", {})
    image_path = image_settings.get("path", None)
    pixel_size = image_settings.get("pixel_size", 7)
    speed = image_settings.get("speed", 200)
    character_set = image_settings.get("character_set", "29EKIMCUMHURIYETBAYRAMI")
    
    #signature
    signature = settings.get("signature", "sametaliyalcin")
    
    #program settings
    program_settings = settings.get("program", {})
    program_title = program_settings.get("title", "29EKIMCUMHURIYETBAYRAMI")
    background_color = program_settings.get("background_color", "black")
    
    
    if __name__ == "__main__":
        if not image_path:
            print("Error: 'image_path' is not specified in the settings.json file.")
            exit(1)
        
        root = tk.Tk()
        app = ImageDrawing(root, image_path, pixel_size, speed, signature, character_set, program_title, background_color, tk)
        root.mainloop()