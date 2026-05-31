from PIL import Image
import os

source_path = '/home/sourab/.gemini/antigravity/brain/2ee04cf4-f2b9-470c-97cb-6cc12c6ac68d/media__1777894840495.png'
base_dest_path = '/home/sourab/Documents/vyoma_lab_website/images/people/alumni/postdoc'

sizes = {
    'sm': 400,
    'md': 800,
    'lg': 1600,
    'placeholder': 400
}

img = Image.open(source_path)
# Ensure it's RGB for webp
if img.mode in ('RGBA', 'P'):
    img = img.convert('RGB')

for name, width in sizes.items():
    dest_dir = os.path.join(base_dest_path, name)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, 'n-srikrishna.webp')
    
    # Calculate height to maintain aspect ratio
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    
    resized_img = img.resize((width, h_size), Image.Resampling.LANCZOS)
    resized_img.save(dest_path, 'WEBP', quality=90 if name != 'placeholder' else 10)
    print(f'Saved {dest_path} ({width}x{h_size})')
