from PIL import Image

p2 = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793265021441_6faef274.png"
im2 = Image.open(p2).convert("RGBA")
W, H = im2.size

# In Image 2, the grey hoodie is turned front!
# Let's find horizontal range for this hoodie and coat
for x in range(W):
    pass

# Let's check non-white columns around x=80..400
col_occupied = []
for x in range(W):
    occ = any(im2.getpixel((x, y))[0] < 240 for y in range(120, H-20, 5))
    col_occupied.append(occ)

# print segments in im2
segments = []
in_seg = False
start_x = 0
for x in range(W):
    if col_occupied[x] and not in_seg:
        in_seg = True
        start_x = x
    elif not col_occupied[x] and in_seg:
        in_seg = False
        segments.append((start_x, x))
if in_seg:
    segments.append((start_x, W - 1))

print("Image 2 segments:")
for idx, (s, e) in enumerate(segments):
    print(f"Seg {idx}: x={s}..{e} (width {e-s})")
