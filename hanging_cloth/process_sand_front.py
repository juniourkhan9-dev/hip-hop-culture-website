import os
from PIL import Image

p = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793265404664_a891eba6.png"
im = Image.open(p).convert("RGBA")
print("Uploaded front beige sweatshirt size:", im.size)

# Crop rod out (rod is at top around y=0..60)
# Let's inspect where rod ends and hook starts
# Find non-white pixels
w, h = im.size

# Let's clean white background
pixels = im.load()
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if r >= 246 and g >= 246 and b >= 246:
            pixels[x, y] = (255, 255, 255, 0)
        elif r >= 235 and g >= 235 and b >= 235:
            avg = (r + g + b) / 3.0
            alpha = int(255 * max(0.0, min(1.0, (255 - avg) / 20.0)))
            pixels[x, y] = (r, g, b, alpha)

# Also remove rod if at top:
for y in range(min(55, h)):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        # Rod is horizontal bar across top
        if y < 45 and (x < w*0.35 or x > w*0.48):
            pixels[x, y] = (0, 0, 0, 0)

bbox = im.getbbox()
if bbox:
    im = im.crop(bbox)

out_path = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\real_products\sand_front_exact.png"
im.save(out_path)
print("Saved sand_front_exact.png with size:", im.size)
