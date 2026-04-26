from PIL import Image, ImageChops
import os

def trim(im):
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im.convert("RGB"), bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

def process_and_trim(base_path, name):
    target_path = os.path.join(base_path, "lg", name)
    if not os.path.exists(target_path):
        print(f"File not found: {target_path}")
        return
        
    with Image.open(target_path) as img:
        # Trim white space
        trimmed = trim(img)
        
        # Save back to lg, md, sm
        widths = {'lg': 1600, 'md': 800, 'sm': 400, 'placeholder': 20}
        for size_name, width in widths.items():
            # Scale maintain aspect ratio
            w_percent = (width / float(trimmed.size[0]))
            # Cap w_percent so it doesn't upscale too much if trimmed is small
            # Actually, let's just scale.
            h_size = int((float(trimmed.size[1]) * float(w_percent)))
            
            resized = trimmed.resize((width, h_size), Image.Resampling.LANCZOS)
            
            target_dir = os.path.join(base_path, size_name)
            os.makedirs(target_dir, exist_ok=True)
            resized.save(os.path.join(target_dir, name), "WEBP", quality=85)
            print(f"Processed {size_name}/{name}")

base = "/home/sourab/Documents/vyoma_lab_website/images/facilities"
process_and_trim(base, "thermal-imaging.webp")
