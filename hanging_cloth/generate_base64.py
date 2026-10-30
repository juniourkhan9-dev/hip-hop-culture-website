import base64
import os

assets_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets"
crops = {}
for i in range(10):
    p = os.path.join(assets_dir, f"item_{i}.png")
    if os.path.exists(p):
        with open(p, "rb") as f:
            crops[f"item_{i}"] = base64.b64encode(f.read()).decode('utf-8')

# save to a js file
with open(os.path.join(assets_dir, "crops.js"), "w") as f:
    f.write("const CROP_IMAGES = ")
    import json
    f.write(json.dumps(crops))
    f.write(";\n")

print("Generated crops.js with count:", len(crops))
