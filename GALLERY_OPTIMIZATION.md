# Gallery Image Optimization Guide

This document outlines the techniques used to optimize the Vyoma Lab gallery. These steps can be implemented in a backend processing pipeline (e.g., using Python/Pillow, Node.js/Sharp, or Go/Image) to handle new image uploads automatically.

## 1. Image Processing Workflow

For every uploaded high-resolution image, four distinct versions should be generated:

| Version | Max Width | Purpose | Quality (WebP) |
| :--- | :--- | :--- | :--- |
| **Large (`lg`)** | 1600px | High-res Lightbox / Full-screen | 80 |
| **Medium (`md`)** | 800px | Desktop grid / Tablets | 80 |
| **Small (`sm`)** | 400px | Mobile grid | 80 |
| **Placeholder** | 20px | Blur-up placeholder (LQIP) | 10 |

### Why WebP?
WebP provides superior compression compared to JPEG and PNG. It supports transparency and generally results in file sizes that are **25-35% smaller** for the same visual quality.

---

## 2. The "Blur-Up" Technique

To achieve a perceived "instant" load, we use the tiny **20px placeholder**.

1. **CSS Background**: Set the placeholder as a `background-image` on the card container (centered and covering the space).
2. **Initial State**: The main `<img>` is set to `opacity: 0` and `filter: blur(10px)`.
3. **Transition**: When the main image finishes loading, the browser triggers an `onload` event.
4. **Final State**: JavaScript adds a `.loaded` class to the image, which changes `opacity` to `1` and `blur` to `0` with a smooth CSS transition.

---

## 3. HTML Implementation (`srcset`)

Use the `srcset` attribute to let the browser decide which file to download based on the user's screen density and viewport width.

```html
<div class="gallery-card" style="background-image: url('placeholder.webp');">
  <img 
    src="sm/image.webp" 
    srcset="sm/image.webp 400w, md/image.webp 800w, lg/image.webp 1600w"
    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
    data-large-src="lg/image.webp"
    loading="lazy"
    onload="this.classList.add('loaded')"
    alt="..."
  />
</div>
```

- **`sizes`**: Tells the browser how much space the image will occupy on the screen at different breakpoints.
- **`loading="lazy"`**: Native browser feature that delays loading off-screen images until the user scrolls near them.
- **`data-large-src`**: Used by the Lightbox script to fetch the highest resolution only when needed.

---

## 4. Backend Implementation (Python Example)

If using Python (Pillow), the logic follows this pattern:

```python
from PIL import Image

def process_upload(input_path, output_dir):
    sizes = {'sm': 400, 'md': 800, 'lg': 1600, 'placeholder': 20}
    with Image.open(input_path) as img:
        img = img.convert("RGB") # Ensure format
        for name, width in sizes.items():
            # Maintain aspect ratio
            w_percent = (width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            resized = img.resize((width, h_size), Image.Resampling.LANCZOS)
            
            quality = 10 if name == 'placeholder' else 80
            resized.save(f"{output_dir}/{name}/image.webp", "WEBP", quality=quality)
```

---

## 5. UI/UX Considerations
- **Aspect Ratios**: Ensure the backend crops or letterboxes images if a strict grid is required, or use Masonry (like we did) to allow varying heights.
- **Color Profile**: Always strip EXIF data (metadata) to save extra kilobytes and ensure sRGB color profile for web consistency.
