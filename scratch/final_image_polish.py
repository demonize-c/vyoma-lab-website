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

def center_image(im, size=(1600, 1600)):
    # Create a white canvas
    canvas = Image.new('RGB', size, (255, 255, 255))
    
    # Scale product to fit canvas with padding
    target_padding = 100
    max_w = size[0] - (2 * target_padding)
    max_h = size[1] - (2 * target_padding)
    
    w, h = im.size
    ratio = min(max_w/w, max_h/h)
    new_size = (int(w * ratio), int(h * ratio))
    
    im_resized = im.resize(new_size, Image.Resampling.LANCZOS)
    
    # Calculate position
    offset = ((size[0] - new_size[0]) // 2, (size[1] - new_size[1]) // 2)
    canvas.paste(im_resized, offset)
    return canvas

def process_file(base_path, filename):
    lg_path = os.path.join(base_path, "lg", filename)
    if not os.path.exists(lg_path):
        return
        
    with Image.open(lg_path) as img:
        # Step 1: Special case for homogenizer (crop the bucket)
        if "homogenizer" in filename:
            # Crop the left 70% of the image to remove the bucket on the right
            crop_w = int(img.size[0] * 0.7)
            img = img.crop((0, 0, crop_w, img.size[1]))
            
        # Step 2: Trim white space
        trimmed = trim(img)
        
        # Step 3: Center on square canvas
        centered = center_image(trimmed)
        
        # Step 4: Save all sizes
        widths = {'lg': 1600, 'md': 800, 'sm': 400, 'placeholder': 20}
        for name, width in widths.items():
            w_percent = (width / float(centered.size[0]))
            h_size = int((float(centered.size[1]) * float(w_percent)))
            resized = centered.resize((width, h_size), Image.Resampling.LANCZOS)
            
            target_dir = os.path.join(base_path, name)
            os.makedirs(target_dir, exist_ok=True)
            resized.save(os.path.join(target_dir, filename), "WEBP", quality=85)
            print(f"Processed {name}/{filename}")

base = "/home/sourab/Documents/vyoma_lab_website/images/facilities"
files = ["impedance-tube.webp", "ball-milling.webp", "high-shear-homogenizer.webp", "bulk-density.webp"]

for f in files:
    process_file(base, f)
