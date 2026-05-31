from PIL import Image, ImageDraw, ImageFont

# Open the original reference image
img = Image.open("scratch/ref.jpg").convert("RGBA")

# 1. Crop to remove the black text at the bottom.
# Assuming the orange emblem + orange text takes up the top ~60% of the image.
# Image is 225x225. Let's crop to 225 x 140.
img = img.crop((0, 0, 225, 130))

# 2. Trim excess white space around the cropped image
# Find bounding box of non-white pixels
bg = Image.new(img.mode, img.size, (255, 255, 255, 255))
diff = Image.composite(img, bg, img)
# Get bounding box of anything not purely white
def get_bbox(image):
    data = image.getdata()
    w, h = image.size
    left, top, right, bottom = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            r,g,b,a = data[y*w + x]
            if r < 240 or g < 240 or b < 240: # If pixel is not white
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)
    return (left, top, right + 1, bottom + 1)

bbox = get_bbox(img)
if bbox[2] > bbox[0] and bbox[3] > bbox[1]:
    img = img.crop(bbox)

# 3. Make the white background transparent
data = img.getdata()
new_data = []
for item in data:
    if item[0] > 230 and item[1] > 230 and item[2] > 230:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
img.putdata(new_data)

# 4. Create new image with space for our custom text
padding = 10
font_size = 18
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
except:
    font = ImageFont.load_default()

text = "Department of Health Research"
temp_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
text_bbox = temp_draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

new_width = max(img.width, text_width) + 20
new_height = img.height + text_height + padding * 3

new_img = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))

# Paste emblem centered
paste_x = (new_width - img.width) // 2
new_img.paste(img, (paste_x, padding))

# Draw text centered below
draw = ImageDraw.Draw(new_img)
text_x = (new_width - text_width) // 2
text_y = img.height + padding * 2
orange_color = (235, 105, 11, 255) # Match the emblem
draw.text((text_x, text_y), text, font=font, fill=orange_color)

# Save
new_img.save("images/funding/dhr-logo-new.png")
print("Saved cleanly cropped logo to images/funding/dhr-logo-new.png")
