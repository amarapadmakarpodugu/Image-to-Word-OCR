# 📝 OCR Image to Word

A Python-based Optical Character Recognition (OCR) application that
extracts text from images and converts the extracted text into a
Microsoft Word document.

The project combines **Tesseract OCR** with **OpenCV image
preprocessing** to improve text recognition. It supports both
**English and Telugu**, including images containing mixed Telugu and
English text.

---

## 📌 About the Project

Converting text from an image into editable text manually can be
time-consuming. This project automates the process by taking an image
as input, preprocessing it to improve its quality, extracting the text
using OCR, and finally saving the extracted content into a Word
document.

The application is designed as a simple command-line Python project
that demonstrates the practical use of:

- Python
- Image Processing
- Optical Character Recognition
- Tesseract OCR
- OpenCV
- Word Document Generation

---

## 🎯 Objective

The main objective of this project is to create a simple and effective
system that can:

1. Accept an image containing text.
2. Improve the image using preprocessing techniques.
3. Extract text using Tesseract OCR.
4. Support Telugu and English text recognition.
5. Convert the extracted text into an editable Word document.

---

## ✨ Features

### 🔹 Image to Text Conversion

The application extracts text directly from an image using Tesseract
OCR.

### 🔹 Telugu OCR Support

The project supports Telugu text recognition using the Tesseract
Telugu language data.

### 🔹 English OCR Support

English text can also be recognized using the English Tesseract
language data.

### 🔹 Telugu + English OCR

The application uses:

```python
lang="tel+eng"
