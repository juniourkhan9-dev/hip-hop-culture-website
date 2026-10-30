import os
from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Segments found:
# 1: x=30 to x=101   -> item 0 (Black hoodie)
# 2: x=132 to x=289  -> item 1 (Double breasted coat)
# 3: x=318 to x=396  -> item 2 (Grey hoodie)
# 4: x=406 to x=470  -> item 3 (Sand hoodie)
# 5: x=481 to x=567  -> item 4 (Green hoodie)
# 6: x=578 to x=645  -> item 5 (Black tee)
# 7: x=656 to x=727  -> item 6 (Charcoal hoodie)
# 8: x=739 to x=816  -> item 7 (Grey hoodie 2)
# 9: x=826 to x=891  -> item 8 (Sand hoodie 2)
# 10: x=902 to x=987 -> item 9 (Green hoodie 2)

# But wait, hangers & price tags are at y=80..130!
# Let's inspect where the hanger hook and price tag are for each item:
# Hook is around the center or left of each segment, tag hangs down to about x=seg_start-15 or seg_start.
# Let's check non-white pixels from y=80 to y=360 for each item with safety margins that DO NOT overlap the next item!

# Between item 0 and 1: boundary is around x=115
# Between item 1 and 2: boundary is around x=300
# Between item 2 and 3: boundary is around x=401
# Between item 3 and 4: boundary is around x=475
# Between item 4 and 5: boundary is around x=572
# Between item 5 and 6: boundary is around x=650
# Between item 6 and 7: boundary is around x=733
# Between item 7 and 8: boundary is around x=821
# Between item 8 and 9: boundary is around x=896

clean_ranges = [
    ("item_0", 25, 80, 115, 360),
    ("item_1", 125, 80, 298, 360),
    ("item_2", 310, 80, 401, 360),
    ("item_3", 402, 80, 475, 360),
    ("item_4", 476, 80, 572, 360),
    ("item_5", 573, 80, 650, 360),
    ("item_6", 651, 80, 733, 360),
    ("item_7", 734, 80, 821, 360),
    ("item_8", 822, 80, 896, 360),
    ("item_9", 897, 80, 995, 360),
]

out_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\clean_transparent"
os.makedirs(out_dir, exist_ok=True)

for item_id, x1, y1, x2, y2 in clean_ranges:
    crop = img.crop((x1, y1, x2, y2))
    w, h = crop.size
    
    # Process transparency:
    # Any pixel with r, g, b all >= 245 is pure transparent
    pixels = crop.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r >= 246 and g >= 246 and b >= 246:
                pixels[x, y] = (255, 255, 255, 0)
            elif r >= 235 and g >= 235 and b >= 235:
                avg = (r + g + b) / 3.0
                alpha = int(255 * max(0.0, min(1.0, (255 - avg) / 20.0)))
                pixels[x, y] = (r, g, b, alpha)

    # Let's remove any isolated tiny stray noise columns on left or right edges
    # If an edge column has very few non-transparent pixels, zero them out!
    for x in range(min(5, w)):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 15: # noise artifact from neighbor
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)

    for x in range(max(0, w - 5), w):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 15: # noise artifact
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)

    # Trim empty borders
    bbox = crop.getbbox()
    if bbox:
        crop = crop.crop(bbox)

    out_path = os.path.join(out_dir, f"{item_id}.png")
    crop.save(out_path)
    print(f"Cleaned {item_id}: new size {crop.size}")

print("Clean crops complete!")
