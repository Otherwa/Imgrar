from pygments import highlight
import pngquant
import os
from time import sleep
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import pytesseract
from PIL import Image
import json


# convert infolder
class convert:
    def __init__(self, infolder, outfolder):
        try:
            with open("config.json", "r") as f:
                datajson = json.load(f)
        except:
            Exception("Could not read config.json")

        self.infolder = infolder
        self.outfolder = outfolder
        self.pyquantconfig = datajson["pngquant"]
        self.tesseractconfig = datajson["tesseract"]

        pngquant.config(
            self.pyquantconfig,
            min_quality=5,
            max_quality=5,
        )

        # make folder
        os.makedirs(self.outfolder, exist_ok=True)
        os.makedirs(self.infolder, exist_ok=True)

    def code2png(self):
        print("Png 2 Code")
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
        print("Png 2 Code")
        pytesseract.pytesseract.tesseract_cmd = self.tesseractconfig
        for filename in os.listdir(self.outfolder):
            filepath = os.path.join(self.outfolder, filename)
            img = Image.open(filepath)
            img = img.convert("L")
            text = pytesseract.image_to_string(img)
            file = filename.split(".")
            with open(self.infolder + file[0] + "." + file[1], "w") as file:
                file.write(text)
            print(filepath + " Done ✅")
