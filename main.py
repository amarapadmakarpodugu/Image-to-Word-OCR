from docx import Document
import pytesseract as pa
from PIL import Image
import os

# Ask the user for the image file
image_path = input("Enter the image file path: ")

# Check if the image exists
if not os.path.exists(image_path):
    print("Image file not found!")
    exit()

# Set Tesseract path
# Change this only if Tesseract is installed in a different location
pa.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Extract text from image
text = pa.image_to_string(Image.open(image_path))

# Create Word document
doc = Document()

for line in text.split("\n"):
    doc.add_paragraph(line)

# Save Word document
output_file = "AUTOWRITE.docx"
doc.save(output_file)

# Check if document was created
if os.path.exists(output_file):
    print("Document saved successfully!")
    print("File:", output_file)
else:
    print("Document was not saved!")