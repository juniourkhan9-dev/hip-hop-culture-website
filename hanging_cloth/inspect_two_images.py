from PIL import Image

p1 = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793263980955_08ee0ea4.png"
p2 = r"C:\Users\advance computer\.gemini\antigravity\brain\8d3a9cd3-31fe-4d39-a9ab-a2c8f8f040e1\.user_uploaded\media_1793265021441_6faef274.png"

im1 = Image.open(p1)
im2 = Image.open(p2)
print("Image 1 size:", im1.size)
print("Image 2 size:", im2.size)
