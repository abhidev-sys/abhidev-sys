from PIL import Image
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------

INPUT_IMAGE = Path("assets/source-prepped.png")

ASCII_WIDTH = 100

ASCII_RAMP = " .`:-=+*cs#%@"

# ----------------------------
# Load Image
# ----------------------------

image = Image.open(INPUT_IMAGE)

print("Image Loaded Successfully")
print("Original Size :", image.size)
print("Mode :", image.mode)

# ----------------------------
# Resize Image
# ----------------------------

width, height = image.size

aspect_ratio = height / width

ascii_height = int(ASCII_WIDTH * aspect_ratio * 0.55)

image = image.resize((ASCII_WIDTH, ascii_height))

print("\nImage Resized Successfully")
print("New Size :", image.size)

# ----------------------------
# Convert to Grayscale
# ----------------------------

image = image.convert("L")

print("\nConverted to Grayscale")
print("Mode :", image.mode)

# ----------------------------
# Convert Pixels to ASCII
# ----------------------------

pixels = list(image.getdata())

ascii_data = []

for pixel in pixels:

    index = (255 - pixel) * (len(ASCII_RAMP) - 1) // 255

    ascii_data.append(ASCII_RAMP[index])

print("\nASCII Characters Generated")
print("Total Characters :", len(ascii_data))

# ----------------------------
# Create ASCII Rows
# ----------------------------

ascii_rows = []

for i in range(0, len(ascii_data), ASCII_WIDTH):
    row = "".join(ascii_data[i:i + ASCII_WIDTH])
    ascii_rows.append(row)

print("\nASCII Rows Created")
print("Total Rows :", len(ascii_rows))

print("\nFirst 5 Rows:\n")

for row in ascii_rows[:5]:
    print("|" + row + "|")