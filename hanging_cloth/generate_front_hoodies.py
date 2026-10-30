import os
from PIL import Image

src_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\real_products"
front_hoodie_path = os.path.join(src_dir, "grey_hoodie_front.png")
im = Image.open(front_hoodie_path).convert("RGBA")

# Colors for other items:
# item 0: Black (#2b2b2b)
# item 3: Sand (#d8c7ad)
# item 4: Green (#1c4a2a)
# item 6: Charcoal (#343538)
# item 8: Oatmeal (#dcd1bc)
# item 9: Emerald (#154428)

def colorize_hoodie(base_im, target_rgb, out_path, is_text_preserved=False):
    # base_im is grey hoodie (average grey intensity around 180-210)
    w, h = base_im.size
    res = Image.new("RGBA", (w, h))
    pixels = base_im.load()
    out_pixels = res.load()
    
    tr, tg, tb = target_rgb
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0:
                out_pixels[x, y] = (0, 0, 0, 0)
                continue
            
            # Check if hanger hook/wood/tag
            # Tag is top right (x > w/2 and y < 65) with white tag & black string
            # Wooden hanger is at top (y < 45)
            # If pixel is near white tag
            if y < 65 and r > 220 and g > 220 and b > 200:
                out_pixels[x, y] = (r, g, b, a) # preserve tag
                continue
            if y < 45 and (r > 60 and g < 50): # preserve wooden hanger
                out_pixels[x, y] = (r, g, b, a)
                continue
            if y < 65 and r < 50 and g < 50 and b < 50 and x > w*0.5: # tag text/hole
                out_pixels[x, y] = (r, g, b, a)
                continue

            # Drawstring check (drawstrings are white around x=w*0.4..0.6, y=30..110)
            if y < 110 and x > w*0.42 and x < w*0.58 and r > 210 and g > 210 and b > 210:
                out_pixels[x, y] = (r, g, b, a) # preserve white drawstrings
                continue

            # Check if Atheist text (black letters around y=95..165)
            if not is_text_preserved and (y > 90 and y < 165 and x > w*0.25 and x < w*0.75):
                if r < 80 and g < 80 and b < 80:
                    # Let's blend out text for plain hoodies by matching nearby fabric intensity
                    intensity = 0.75
                    out_pixels[x, y] = (int(tr * intensity), int(tg * intensity), int(tb * intensity), a)
                    continue

            # For the fabric: multiply/tint based on grey intensity
            grey_val = (r * 0.299 + g * 0.587 + b * 0.114) / 195.0
            new_r = min(255, int(tr * grey_val))
            new_g = min(255, int(tg * grey_val))
            new_b = min(255, int(tb * grey_val))
            out_pixels[x, y] = (new_r, new_g, new_b, a)
            
    res.save(out_path)
    print(f"Generated {out_path}")

# Generate front views:
colorize_hoodie(im, (38, 38, 38), os.path.join(src_dir, "black_hoodie_front.png"))
colorize_hoodie(im, (216, 199, 173), os.path.join(src_dir, "sand_hoodie_front.png"))
colorize_hoodie(im, (26, 72, 40), os.path.join(src_dir, "green_hoodie_front.png"))
colorize_hoodie(im, (50, 52, 54), os.path.join(src_dir, "charcoal_hoodie_front.png"))
colorize_hoodie(im, (220, 209, 188), os.path.join(src_dir, "oatmeal_hoodie_front.png"))
colorize_hoodie(im, (21, 68, 40), os.path.join(src_dir, "emerald_hoodie_front.png"))

print("All photorealistic front views generated!")
