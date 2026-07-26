from rembg import remove
from PIL import Image
import cv2
import numpy as np
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
INPUT = Path("assets/source-photo.jpg")
OUTPUT = Path("assets/source-prepped.png")

# -----------------------------
# Remove Background
# -----------------------------
img = Image.open(INPUT).convert("RGBA")
img_no_bg = remove(img)

# -----------------------------
# Composite on White Background
# -----------------------------
white = Image.new("RGBA", img_no_bg.size, (255, 255, 255, 255))
white.paste(img_no_bg, mask=img_no_bg)

rgb = white.convert("RGB")

# -----------------------------
# Convert to OpenCV
# -----------------------------
cv_img = cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2BGR)

gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# CLAHE Contrast Enhancement
# -----------------------------
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

enhanced = clahe.apply(gray)

# -----------------------------
# Save
# -----------------------------
cv2.imwrite(str(OUTPUT), enhanced)

print(f"✅ Saved -> {OUTPUT}")