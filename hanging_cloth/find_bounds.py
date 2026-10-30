from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")
W, H = img.size

# Let's inspect horizontal bounds: find columns that have non-white pixels
# Rod is at y=85..105, let's look at y=130..340 (garment bodies)
profile_y_start = 130
profile_y_end = 340

cols_occupied = []
for x in range(W):
    is_garment = False
    for y in range(profile_y_start, profile_y_end, 5):
        r, g, b, a = img.getpixel((x, y))
        if r < 240 or g < 240 or b < 240:
            is_garment = True
            break
    cols_occupied.append(is_garment)

# Find contiguous segments of True
segments = []
in_seg = False
start_x = 0
for x in range(W):
    if cols_occupied[x] and not in_seg:
        in_seg = True
        start_x = x
    elif not cols_occupied[x] and in_seg:
        in_seg = False
        segments.append((start_x, x))
if in_seg:
    segments.append((start_x, W - 1))

print(f"Found {len(segments)} segments:")
for idx, (s, e) in enumerate(segments):
    print(f"Segment {idx}: x={s} to x={e} (width {e-s})")
