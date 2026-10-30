import base64
import os
import json

trans_dir = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\transparent"
out_js = r"C:\Users\advance computer\.gemini\antigravity\scratch\clothing-rack-showcase\assets\transparent_crops.js"

data = {}
for i in range(10):
    fpath = os.path.join(trans_dir, f"item_{i}.png")
    with open(fpath, "rb") as f:
        data[f"item_{i}"] = base64.b64encode(f.read()).decode("utf-8")

with open(out_js, "w") as f:
    f.write("const TRANSPARENT_ITEMS = ")
    f.write(json.dumps(data))
    f.write(";\n")

print("Created transparent_crops.js with 10 items!")
