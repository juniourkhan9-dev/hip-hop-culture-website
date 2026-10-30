from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Let's check non-white pixels between y=80 and y=115 for item 0 (x=25..110)
print("Item 0 elements between y=80 and y=120:")
for y in range(80, 115):
    non_white_cols = [x for x in range(25, 110) if img.getpixel((x, y))[0] < 240]
    if non_white_cols:
        print(f"y={y}: non-white x={min(non_white_cols)}..{max(non_white_cols)} (count {len(non_white_cols)})")
