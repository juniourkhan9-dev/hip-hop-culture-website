import os
from PIL import Image

clean_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\clean_transparent"
src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Let's see the height and top rows of item_0..9
# In the original image:
# Rod is at y=85 to y=105.
# Hanger hook loops OVER the rod (from y=85 upwards to ~y=88, and downwards).
# But at y=88..105, the main rod runs horizontally across all items!
# So any crop starting from y=80 includes a piece of the horizontal rod!
# That's why each item image has a little piece of the rod at the top!
# And because there is also the main long rod in HTML, they overlap and look double!

# Let's inspect where the hanger hook meets the rod vs where the hook ends.
# What if we erase the horizontal rod bar from the item images, leaving ONLY the hook (or starting right at/under the rod)?
# Let's inspect the y coordinates of the rod:
# In the original image, rod is between y=87 and y=102.
print("Original image size:", img.size)

for i in range(10):
    fpath = os.path.join(clean_dir, f"item_{i}.png")
    if os.path.exists(fpath):
        im = Image.open(fpath)
        print(f"item_{i} size: {im.size}")
