import base64
import sys
from PIL import Image
import numpy as np

with open('/home/sourab/Documents/vyoma_lab_website/images/logo-transparent.svg', 'r') as f:
    data = f.read()
    
b64 = data.split('base64,')[1].split('"')[0]

img_data = base64.b64decode(b64)
with open('/home/sourab/Documents/vyoma_lab_website/scratch/logo.png', 'wb') as f:
    f.write(img_data)

img = Image.open('/home/sourab/Documents/vyoma_lab_website/scratch/logo.png').convert("RGBA")
arr = np.array(img)

# Find bounding boxes of non-transparent components
alpha = arr[:, :, 3]
non_empty = alpha > 0

import cv2
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(non_empty.astype(np.uint8))

print("Total components:", num_labels - 1)
for i in range(1, num_labels):
    print(f"Component {i}: x={stats[i, cv2.CC_STAT_LEFT]}, y={stats[i, cv2.CC_STAT_TOP]}, w={stats[i, cv2.CC_STAT_WIDTH]}, h={stats[i, cv2.CC_STAT_HEIGHT]}, area={stats[i, cv2.CC_STAT_AREA]}")
