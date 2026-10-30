import os
from PIL import Image

src_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\real_products"
hoodie_front_path = os.path.join(src_dir, "black_hoodie_front.png")
hoodie = Image.open(hoodie_front_path).convert("RGBA")
w, h = hoodie.size

# Tee crop: crewneck without hood, short sleeves
# Let's create black_tee_front.png
tee = hoodie.copy()
pix = tee.load()

# Hollow out hood above shoulders (y < 42, except hanger at top)
for y in range(45):
    for x in range(w):
        r, g, b, a = pix[x, y]
        # if fabric (not wooden hanger or tag)
        if a > 0 and y > 15 and not (x > w*0.55 and y < 35):
            if r < 60 and g < 60 and b < 60:
                pix[x, y] = (0, 0, 0, 0)

# Short sleeves (remove sleeve fabric on lower half below y=120)
for y in range(120, h):
    for x in range(w):
        if x < w*0.18 or x > w*0.82:
            pix[x, y] = (0, 0, 0, 0)

tee.save(os.path.join(src_dir, "black_tee_front.png"))
print("Saved black_tee_front.png")
