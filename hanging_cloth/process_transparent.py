import os
from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")
W, H = img.size

# Each crop contains white background. We want clean transparent PNGs where white (#ffffff or close to #ffffff) is turned into 0 alpha!
# Also, let's carefully crop each item so there is no leakage from neighboring items.

items_coords = [
    # (id, x1, y1, x2, y2)
    ("item_0", 25, 78, 110, 360),
    ("item_1", 124, 78, 292, 360),
    ("item_2", 305, 78, 395, 360),
    ("item_3", 390, 78, 468, 360),
    ("item_4", 465, 78, 550, 360),
    ("item_5", 555, 78, 638, 360),
    ("item_6", 635, 78, 715, 360),
    ("item_7", 715, 78, 805, 360),
    ("item_8", 802, 78, 878, 360),
    ("item_9", 876, 78, 970, 360),
]

out_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\transparent"
os.makedirs(out_dir, exist_ok=True)

def remove_white_bg(im, tolerance=245):
    # Convert pixels that are near white (r > 245 and g > 245 and b > 245) to transparent
    # Also handle anti-aliasing / soft edge
    data = im.getdata()
    new_data = []
    for item in data:
        r, g, b, a = item
        # If it's near white background
        if r >= 248 and g >= 248 and b >= 248:
            new_data.append((255, 255, 255, 0))
        elif r >= 235 and g >= 235 and b >= 235:
            # Soft edge transparency
            avg = (r + g + b) / 3.0
            alpha = int(255 * max(0.0, min(1.0, (255 - avg) / (255 - 235))))
            new_data.append((r, g, b, min(a, alpha)))
        else:
            new_data.append((r, g, b, a))
    
    im.putdata(new_data)
    # Autocrop transparent borders
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    return im

for item_id, x1, y1, x2, y2 in items_coords:
    crop = img.crop((x1, y1, x2, y2))
    transparent_crop = remove_white_bg(crop)
    out_file = os.path.join(out_dir, f"{item_id}.png")
    transparent_crop.save(out_file)
    print(f"Saved {item_id}: {transparent_crop.size}")

print("All transparent crops generated successfully!")
