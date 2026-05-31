import urllib.request
from PIL import Image, ImageDraw, ImageFont

# 1. Download the reference image
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4n3dYGI_GHoIUVEt1bPhvRNatyInbUkkHbA&s"
urllib.request.urlretrieve(url, "scratch/ref.jpg")

# 2. Open image and convert to RGBA
img = Image.open("scratch/ref.jpg").convert("RGBA")

# 3. Create a new image with extra space at the bottom for the text
new_width = img.width + 100
new_height = img.height + 60
new_img = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))

# Paste the original emblem in the top center
paste_x = (new_width - img.width) // 2
new_img.paste(img, (paste_x, 0))

# 4. Remove white background (make it transparent)
data = new_img.getdata()
new_data = []
for item in data:
    # If the pixel is mostly white, make it transparent
    if item[0] > 230 and item[1] > 230 and item[2] > 230:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
new_img.putdata(new_data)

# 5. Draw the text "Department of Health Research"
draw = ImageDraw.Draw(new_img)
try:
    # Try to load a clean sans-serif font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
except:
    font = ImageFont.load_default()

text = "Department of Health Research"
# Get text bounding box
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Calculate text position (centered, below the image)
text_x = (new_width - text_width) // 2
text_y = img.height + 10

# Orange color matching the emblem
orange_color = (235, 105, 11, 255)

draw.text((text_x, text_y), text, font=font, fill=orange_color)

# Save
new_img.save("images/funding/dhr-logo-new.png")
print("Saved as images/funding/dhr-logo-new.png")
