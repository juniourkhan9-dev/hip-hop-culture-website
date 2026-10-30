import os
from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")
W, H = img.size

# We have 10 items hanging along the rod:
# 0: black hoodie side (left)
# 1: black suit jacket front
# 2: grey hoodie side
# 3: beige hoodie side
# 4: green hoodie side
# 5: black t-shirt side
# 6: dark washed hoodie side
# 7: grey hoodie side (second)
# 8: beige hoodie side (second)
# 9: green hoodie side (second)

# Let's define approximate bounding boxes (x1, y1, x2, y2) for each item including hanger and tag:
# Total width is 1024, height 367.
# Rod is around y=85 to y=105. Hanger hook starts around y=85.
# Clothing hangs down to y=350.

items_boxes = [
    # (id, name, type, x1, y1, x2, y2)
    ("item_0", "Faded Black Hoodie", "hoodie_black", 25, 80, 105, 355),
    ("item_1", "Double Breasted Wool Coat", "coat_front", 125, 80, 290, 355),
    ("item_2", "Heather Grey Hoodie", "hoodie_grey", 305, 80, 395, 355),
    ("item_3", "Sand Heavyweight Hoodie", "hoodie_beige", 390, 80, 470, 355),
    ("item_4", "Forest Green Hoodie", "hoodie_green", 465, 80, 550, 355),
    ("item_5", "Classic Black Tee", "tee_black", 555, 80, 638, 355),
    ("item_6", "Washed Charcoal Hoodie", "hoodie_charcoal", 635, 80, 715, 355),
    ("item_7", "Athletic Grey Hoodie", "hoodie_grey2", 715, 80, 805, 355),
    ("item_8", "Oatmeal Hoodie", "hoodie_beige2", 800, 80, 880, 355),
    ("item_9", "Emerald Green Hoodie", "hoodie_green2", 875, 80, 970, 355),
]

out_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets"
os.makedirs(out_dir, exist_ok=True)

# Also let's extract the header & rod background if needed, or save individual item sprites
for item_id, name, itype, x1, y1, x2, y2 in items_boxes:
    crop = img.crop((x1, y1, x2, y2))
    crop.save(os.path.join(out_dir, f"{item_id}.png"))
    print(f"Saved {item_id}: {crop.size}")

# Also let's save the whole rod / bar as background
# Bar spans from x=0 to 1024, y=70 to 115
bar = img.crop((0, 70, 1024, 115))
bar.save(os.path.join(out_dir, "bar.png"))

print("Extracted successfully!")
