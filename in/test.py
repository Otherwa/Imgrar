from pygments import highlight
import pngquant
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

with open(
    "C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\Imgrar\\test\\test.py", "rb"
) as file:
    code = file.read()
lexer = PythonLexer()
formatter = ImageFormatter(font_name="Courier New", font_size=16)
image_data = highlight(code, lexer, formatter)
with open(
    "C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\Imgrar\\test\\convert.png", "wb"
) as file:
    file.write(image_data)

# compress
pngquant.config("C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\pngquant\\pngquant.exe")
pngquant.quant_image(
    "C:\\Users\\athar\\OneDrive\\Desktop\\Dev\\Imgrar\\test\\convert.png"
)
# lol
