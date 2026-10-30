import os
from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Safe item horizontal ranges in original image:
clean_ranges = [
    ("item_0", 25, 93, 115, 360),
    ("item_1", 125, 93, 298, 360),
    ("item_2", 310, 93, 401, 360),
    ("item_3", 402, 93, 475, 360),
    ("item_4", 476, 93, 572, 360),
    ("item_5", 573, 93, 650, 360),
    ("item_6", 651, 93, 733, 360),
    ("item_7", 734, 93, 821, 360),
    ("item_8", 822, 93, 896, 360),
    ("item_9", 897, 93, 985, 360),
]

out_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\clean_transparent"
os.makedirs(out_dir, exist_ok=True)

for item_id, x1, y1, x2, y2 in clean_ranges:
    crop = img.crop((x1, y1, x2, y2))
    w, h = crop.size
    pixels = crop.load()

    # If y=93..94 still has some residual rod shadow at the top 2-3 rows, let's remove any non-hook horizontal line:
    # Rod is across the top. Hook is just 2-3 pixels wide!
    for y in range(min(5, h)):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # If it's a grey rod pixel near top
            if y < 3 and (r < 240 and abs(r - g) < 10 and abs(g - b) < 10):
                # Check if this column is part of a wide horizontal block
                pixels[x, y] = (255, 255, 255, 0)

    # Transparency conversion
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r >= 246 and g >= 246 and b >= 246:
                pixels[x, y] = (255, 255, 255, 0)
            elif r >= 235 and g >= 235 and b >= 235:
                avg = (r + g + b) / 3.0
                alpha = int(255 * max(0.0, min(1.0, (255 - avg) / 20.0)))
                pixels[x, y] = (r, g, b, alpha)

    # Edge cleaning
    for x in range(min(6, w)):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 15:
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)

    for x in range(max(0, w - 6), w):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 15:
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)

    # Trim empty bounds
    bbox = crop.getbbox()
    if bbox:
        crop = crop.crop(bbox)

    out_path = os.path.join(out_dir, f"{item_id}.png")
    crop.save(out_path)
    print(f"Item {item_id} clean: size {crop.size}")

print("All rod slices completely removed from images!")
