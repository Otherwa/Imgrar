from pygments import highlight
import pngquant
import os
from time import sleep
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import pytesseract
from PIL import Image


# convert infolder
class convert:
    def __init__(self, infolder, outfolder, pyquantconfig=None, tesseractconfig=None):
        print("Initializing conversion")
        self.infolder = infolder
        self.outfolder = outfolder
        self.pyquantconfig = pyquantconfig
        self.tesseractconfig = tesseractconfig

        pngquant.config(
            pyquantconfig,
            min_quality=5,
            max_quality=5,
        )
        # make folder
        os.makedirs(outfolder, exist_ok=True)
        os.makedirs(infolder, exist_ok=True)

    def code2png(self):
        for filename in os.listdir(self.infolder):
            filepath = os.path.join(self.infolder, filename)
            with open(filepath, "rb") as file:
                code = file.read()

            lexer = PythonLexer()
            formatter = ImageFormatter(font_name="Courier New", font_size=16)
            image_data = highlight(code, lexer, formatter)

            with open(os.path.join(self.outfolder, filename) + ".png", "wb") as file:
                file.write(image_data)

            for i in range(5):
                print(".", end="")
                sleep(0.2)

            pngquant.quant_image(self.outfolder + "\\" + filename + ".png")
            print("\n" + filename + " ✅", end="\n")

            sleep(1)
        print("\nDone 🤖✅")

    def png2code(self):
        pytesseract.pytesseract.tesseract_cmd = self.tesseractconfig
        for filename in os.listdir(self.outfolder):
            filepath = os.path.join(self.outfolder, filename)
            print(filepath)
            img = Image.open(filepath)
            img = img.convert("L")
            text = pytesseract.image_to_string(img)
            print(text)
            file = filename.split(".")
            with open(self.infolder + file[0] + "." + file[1], "w") as file:
                file.write(text)
