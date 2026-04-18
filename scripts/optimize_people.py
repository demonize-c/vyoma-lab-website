import os
from PIL import Image

PEOPLE_ROOT = 'images/people'
SIZES = {
    'sm': 400,
    'md': 800,
    'lg': 1600,
    'placeholder': 20
}

def process_image(input_path, output_base):
    filename = os.path.basename(input_path)
    name_no_ext = os.path.splitext(filename)[0]
    
    with Image.open(input_path) as img:
        # Convert to RGB if necessary (e.g. for PNG with transparency if saving to JPEG, but here we use WebP)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
            
        for s_name, width in SIZES.items():
            out_dir = os.path.join(output_base, s_name)
            os.makedirs(out_dir, exist_ok=True)
            
            # Maintain aspect ratio
            w_percent = (width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            # Resize
            resized = img.resize((width, h_size), Image.Resampling.LANCZOS)
            
            # Quality
            quality = 10 if s_name == 'placeholder' else 80
            output_path = os.path.join(out_dir, f"{name_no_ext}.webp")
            resized.save(output_path, "WEBP", quality=quality)
            print(f"Generated: {output_path}")

def run():
    for root, dirs, files in os.walk(PEOPLE_ROOT):
        # Skip size folders if we are running this again
        if any(s in root for s in SIZES.keys()):
            continue
            
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                # output_base should be the root of the category (e.g. images/people/alumni/phd)
                process_image(input_path, root)

if __name__ == "__main__":
    run()
