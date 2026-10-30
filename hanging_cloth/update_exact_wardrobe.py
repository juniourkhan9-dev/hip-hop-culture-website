import base64
import os
import json

real_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\real_products"
clean_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\clean_transparent"
out_js = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\full_wardrobe_data.js"

sand_front = os.path.join(real_dir, "sand_front_exact.png")

front_mapping = {
    0: os.path.join(real_dir, "black_hoodie_front.png"),
    1: os.path.join(real_dir, "coat_front.png"),
    2: os.path.join(real_dir, "grey_hoodie_front.png"),
    3: sand_front, # User provided exact beige sweatshirt!
    4: os.path.join(real_dir, "green_hoodie_front.png"),
    5: os.path.join(real_dir, "black_tee_front.png"),
    6: os.path.join(real_dir, "charcoal_hoodie_front.png"),
    7: os.path.join(real_dir, "grey_hoodie_front.png"),
    8: sand_front, # Oatmeal beige sweatshirt
    9: os.path.join(real_dir, "emerald_hoodie_front.png"),
}

side_mapping = {
    0: os.path.join(clean_dir, "item_0.png"),
    1: os.path.join(real_dir, "coat_side.png"),
    2: os.path.join(real_dir, "grey_hoodie_side.png"),
    3: os.path.join(clean_dir, "item_3.png"),
    4: os.path.join(clean_dir, "item_4.png"),
    5: os.path.join(clean_dir, "item_5.png"),
    6: os.path.join(clean_dir, "item_6.png"),
    7: os.path.join(clean_dir, "item_7.png"),
    8: os.path.join(clean_dir, "item_8.png"),
    9: os.path.join(clean_dir, "item_9.png"),
}

def to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

data = {}
for i in range(10):
    data[f"item_{i}"] = {
        "side": to_b64(side_mapping[i]),
        "front": to_b64(front_mapping[i])
    }

with open(out_js, "w") as f:
    f.write("const WARDROBE_DATA = ")
    f.write(json.dumps(data))
    f.write(";\n")

print("Updated full_wardrobe_data.js with exact sand sweatshirt!")
