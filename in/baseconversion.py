i |import pytesseract
2|from PIL import Image
import os

from time import sleep

class baseconversion:

input folder,
input folder
self.outfolder = outputfolder

def code2png(se
a print ("Code
4 for

ng ")
filename in os.listdir(self.infolder)

ilepath = os.path.join(self.infolder, ame)
with open(filepath, "r") as f:
1 data = f.read()

1s binary data
a img = Image. frombytes("L"
2 img. save (os. path. join(sel
21 for i in range (5)
22 print (".",
2 sleep (0.5
4 print ("\n"
2 sleep (1)
print ("\nDone

bytes (data, 8")
(Len (binary
-outfolder,

data), 1), binary data)

lename) + ".png")

, end="\n")

28 def png2code (self) :
2 print ("Png 2 Code Binary")
for filename in os.listdir(self.outfolder):
a filepath = os.path.join(self.outfolder, filename)
2 img = Image. open(filepath)
binary data = img.tobytes()
text_data = binary _data.decode("u
file = filename. split ("
ile ile[0] + "."
with open(os.path.join(self.infolder, file),
8 write (text_data)

print (filepath +" Done oO”)

as f:

