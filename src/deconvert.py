import pytesseract
from PIL import Image


__pytesseract__path__ = (
    "C:\\Users\\athar\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
)


pytesseract.pytesseract.tesseract_cmd = __pytesseract__path__
img = Image.open("C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\Imgrar\\out")
img = img.convert("L")
text = pytesseract.image_to_string(img)
print(text)
