from PIL import Image
import os

def process_single_image(input_path, output_base):
    widths = {'lg': 1600, 'md': 800, 'sm': 400, 'placeholder': 20}
    filename = "high-shear-homogenizer.webp"
    
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        for name, width in widths.items():
            # Maintain aspect ratio
            w_percent = (width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            resized = img.resize((width, h_size), Image.Resampling.LANCZOS)
            
            quality = 10 if name == 'placeholder' else 80
            target_dir = os.path.join(output_base, name)
            os.makedirs(target_dir, exist_ok=True)
            
            resized.save(os.path.join(target_dir, filename), "WEBP", quality=quality)
            print(f"Saved {name}/{filename}")

# Target paths
input_file = "/home/sourab/Documents/vyoma_lab_website/scratch/homogenizer_raw.jpg"
base_dir = "/home/sourab/Documents/vyoma_lab_website/images/facilities"

process_single_image(input_file, base_dir)
