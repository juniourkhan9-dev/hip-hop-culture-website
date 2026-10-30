import base64
import os
import json

clean_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\clean_transparent"
out_js = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\transparent_crops.js"

data = {}
for i in range(10):
    fpath = os.path.join(clean_dir, f"item_{i}.png")
    with open(fpath, "rb") as f:
        data[f"item_{i}"] = base64.b64encode(f.read()).decode("utf-8")

with open(out_js, "w") as f:
    f.write("const TRANSPARENT_ITEMS = ")
    f.write(json.dumps(data))
    f.write(";\n")

print("Updated transparent_crops.js with clean images!")
