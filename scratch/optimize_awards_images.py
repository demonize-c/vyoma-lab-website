import os
import subprocess

base_dir = "/home/sourab/Documents/vyoma_lab_website/images/awards"
files = [f for f in os.listdir(base_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and os.path.isfile(os.path.join(base_dir, f))]

sizes = {
    'lg': (1600, 80),
    'md': (800, 80),
    'sm': (400, 80),
    'placeholder': (20, 10)
}

for f in files:
    input_path = os.path.join(base_dir, f)
    filename_no_ext = os.path.splitext(f)[0]
    
    print(f"Optimizing {f}...")
    
    for name, (width, quality) in sizes.items():
        output_dir = os.path.join(base_dir, name)
        output_path = os.path.join(output_dir, filename_no_ext + ".webp")
        
        # Convert to webp with specific width and quality
        try:
            subprocess.run(["convert", input_path, "-quality", str(quality), "-resize", f"{width}>", output_path], check=True)
            print(f"  Created {name}/{filename_no_ext}.webp")
        except Exception as e:
            print(f"  Error creating {name}: {e}")

print("Optimization complete.")
