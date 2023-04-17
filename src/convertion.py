from pygments import highlight
import pngquant
import os
from time import sleep
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

# convert infolder


class convert:
    def __init__(self, infolder, outfolder, pyquantconfig):
        print("Initializing conversion")
        self.infolder = infolder
        self.outfolder = outfolder
        self.pyquantconfig = pyquantconfig

        pngquant.config(
            pyquantconfig,
            min_quality=5,
            max_quality=5,
        )

    def code2png(self):
        for filename in os.listdir(self.infolder):
            filepath = os.path.join(self.infolder, filename)
            with open(filepath, "rb") as file:
                code = file.read()

            lexer = PythonLexer()
            formatter = ImageFormatter(font_name="Courier New", font_size=16)
            image_data = highlight(code, lexer, formatter)

            with open(self.outfolder + "\\" + filename + ".png", "wb") as file:
                file.write(image_data)

            for i in range(5):
                print(".", end="")
                sleep(0.2)

            pngquant.quant_image(self.outfolder + "\\" + filename + ".png")
            print("\n" + filename + " ✅", end="\n")

            sleep(1)
        print("\nDone 🤖✅")
