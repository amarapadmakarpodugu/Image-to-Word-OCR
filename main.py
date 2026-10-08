from docx import Document
import pytesseract as pa
import os
import cv2

# Tesseract OCR path
pa.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get image name and type
iname = input("Enter name of the image: ")
itype = input("Enter (JPG/PNG): ")

iname = iname + "." + itype.lower()

# Read image
image1 = cv2.imread(iname)

# Check whether image exists
if image1 is None:
    print("Image not found! Check the image name and extension.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Upscale image
large = cv2.resize(gray, None, fx=2, fy=2)

# Remove noise
clear = cv2.GaussianBlur(large, (3, 3), 0)

# Convert image to black and white using Otsu thresholding
value, result = cv2.threshold(
    clear,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Perform OCR
text = pa.image_to_string(result, lang="tel+eng")

# Create Word document
doc = Document()
doc.add_paragraph(text)

# Get document name
while True:
    name = input("Enter name of the document: ")
    name = name + ".docx"

    if os.path.exists(name):
        print("Name already exists! Enter another name.")
    else:
        doc.save(name)
        break

# Confirm saving
if os.path.exists(name):
    print("Document saved successfully!")
else:
    print("Document was not saved!")
