import os
from PIL import Image

p1 = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
p2 = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793265021441_6faef274.png"

im1 = Image.open(p1).convert("RGBA")
im2 = Image.open(p2).convert("RGBA")

out_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\real_products"
os.makedirs(out_dir, exist_ok=True)

def make_clean_transparent(crop):
    w, h = crop.size
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
    # edge noise trim
    for x in range(min(5, w)):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 12:
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)
    for x in range(max(0, w - 5), w):
        col_pts = [pixels[x, y][3] for y in range(h) if pixels[x, y][3] > 30]
        if len(col_pts) < 12:
            for y in range(h):
                pixels[x, y] = (255, 255, 255, 0)
    bbox = crop.getbbox()
    return crop.crop(bbox) if bbox else crop

# 1. From im1: Front Coat (item_1_front)
coat_front = im1.crop((128, 93, 292, 360))
coat_front = make_clean_transparent(coat_front)
coat_front.save(os.path.join(out_dir, "coat_front.png"))
print("Saved coat_front:", coat_front.size)

# 2. From im2: Side Coat (item_1_side)
# In im2, seg 2 is x=94..184, rod is around y=48..54
# Let's inspect where the side coat is in im2:
side_coat = im2.crop((92, 54, 186, 310))
side_coat = make_clean_transparent(side_coat)
side_coat.save(os.path.join(out_dir, "coat_side.png"))
print("Saved coat_side:", side_coat.size)

# 3. From im2: Front Grey Hoodie (item_2_front)
# seg 3 is x=212..396
front_grey_hoodie = im2.crop((208, 54, 400, 310))
front_grey_hoodie = make_clean_transparent(front_grey_hoodie)
front_grey_hoodie.save(os.path.join(out_dir, "grey_hoodie_front.png"))
print("Saved grey_hoodie_front:", front_grey_hoodie.size)

# 4. From im1: Side Grey Hoodie (item_2_side)
# In im1, item 2 side is x=310..400, y=93..360
side_grey_hoodie = im1.crop((310, 93, 400, 360))
side_grey_hoodie = make_clean_transparent(side_grey_hoodie)
side_grey_hoodie.save(os.path.join(out_dir, "grey_hoodie_side.png"))
print("Saved grey_hoodie_side:", side_grey_hoodie.size)

print("Real front and side crops extracted successfully!")
