from PIL import Image
import os

IMAGE = 'images/home-page-banner.jpg'
SIZES = {
    'sm': 400,
    'md': 800,
    'lg': 1600,
    'placeholder': 20
}

def run():
    with Image.open(IMAGE) as img:
        img = img.convert("RGB")
        for name, width in SIZES.items():
            out_dir = f'images/{name}'
            os.makedirs(out_dir, exist_ok=True)
            w_percent = (width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            resized = img.resize((width, h_size), Image.Resampling.LANCZOS)
            quality = 10 if name == 'placeholder' else 80
            resized.save(f"{out_dir}/home-page-banner.webp", "WEBP", quality=quality)
            print(f"Generated: images/{name}/home-page-banner.webp")

if __name__ == "__main__":
    run()
