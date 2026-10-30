import os
from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Let's inspect the hanger hook area around y=80..95 for item 0
# Item 0 x is 25..110
crop = img.crop((40, 80, 85, 110))
# Let's see some pixel values
print("Sample pixels from hanger hook area:")
for y in range(0, min(10, crop.height)):
    row = [crop.getpixel((x, y))[:3] for x in range(0, crop.width, 5)]
    # print non-white pixels
    non_white = [p for p in row if p[0] < 240 or p[1] < 240 or p[2] < 240]
    if non_white:
        print(f"y={y}: found non-white:", non_white[:3])
