import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Users\\athar\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
)
img = Image.open("C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\Imgrar\\test\\convert.png")
img = img.convert("L")
text = pytesseract.image_to_string(img)
print(text)
