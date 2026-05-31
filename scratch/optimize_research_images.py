import os
import subprocess

def process_images():
    base_dir = "images/research"
    sizes = {
        "sm": 400,
        "md": 800,
        "lg": 1600,
        "placeholder": 20
    }
    
    # Files to process (using PNG as source)
    images = [
        "biomedical",
        "cryogenic",
        "electronic",
        "extreme_weather",
        "tactical"
    ]
    
    for img_name in images:
        source_path = os.path.join(base_dir, f"{img_name}.png")
        if not os.path.exists(source_path):
            print(f"Source {source_path} not found, checking for webp...")
            source_path = os.path.join(base_dir, f"{img_name}.webp")
            if not os.path.exists(source_path):
                print(f"No source found for {img_name}")
                continue

        for size_name, width in sizes.items():
            dest_dir = os.path.join(base_dir, size_name)
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, f"{img_name}.webp")
            
            print(f"Generating {dest_path} ({width}w)...")
            
            quality = "10" if size_name == "placeholder" else "85"
            
            # Using convert (ImageMagick 6)
            cmd = [
                "convert",
                source_path,
                "-resize", f"{width}x",
                "-quality", quality,
                dest_path
            ]
            
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error processing {img_name} for {size_name}: {e}")

if __name__ == "__main__":
    process_images()
