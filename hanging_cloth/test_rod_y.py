from PIL import Image

src_path = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
img = Image.open(src_path).convert("RGBA")

# Let's inspect x=60 (middle of item 0), around y=70 to 125
for y in range(75, 125):
    # sample 5 pixels around x=60
    pix = [img.getpixel((x, y))[:3] for x in range(55, 65)]
    # rod pixels typically have r~=g~=b in range 80..220 across a wide horizontal band
    print(f"y={y}: x=55..65:", [p[0] for p in pix])
