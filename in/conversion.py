from pygments import highlight
import pngquant.

import os

from time import sleep

from pygments.lexers import PythonLexer

from pygments.formatters import ImageFormatter
import pytesseract

from PIL import Image

import json

3
4
5
6

class convert:
def __init_ (se.
try:
with open("config.json", "r") as £:
1 datajson = json.load(£)
18 except:
Exception("Could not read con:

infolder, outfolder):

g-json")

1 infolder = infolder

2 outfolder = outfolder

23 pyquantconfig = datajson["pngquant"]

24 tesseractconfig = datajson["tesseract"]

25

26 pngquant .config(

27 self.pyquantconfig,

28 min_quality=s,

29 max_quality=5,

30 )

31

32 #

33 os.makedirs(outfolder, exist_ok=True)

34 os.makedirs(infolder, exist_ok=True)

35

36 def code2png (self) :

37 print ("Png 2 Code")

38 for filename in os.listdir(self.infolder):

39 filepath = os.path.join(self.infolder, filename)
40 with open(filepath, "rb") as file:

41 code = file.read()

42

43 lexer = PythonLexer ()

44 formatter = ImageFormatter (font_name="Courier New", font_size=16)
45 image_data = highlight(code, lexer, formatter)
46

47 with open(os.path.join(self.outfolder, filename) + ".png", "wb") as file:
48 file.write (image_data)

49

50 for i in range (5)

51 print(".", end="")

52 sleep (0.2)

53

54 pngquant.quant_image(self.outfolder + "\\" + filename + ".png")
55 print("\n" + filename + "0", end="\n")

56

57 sleep (1)

58 print ("\nDone

59

def png2code (self) :
print ("Png 2 Code")
pytesseract .pytesseract.tesseract_cmd = se
for filename in os.listdir(self.outfolder) :
filepath = os.path.join(self.outfolder, filename)
img = Image.open(filepath)
img = img.convert("L")
text = pytesseract.image_to_string(img)
file = filename.split(".”)
with open(self.infolder + file[0] + "." + file[il, "w") as file:
file.write (text)
print (filepath + " Done O”)

tesseractconfig

