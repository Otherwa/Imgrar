from src.conversion import convert
from src.baseconversion import baseconversion
import argparse

IOWA WINE

if __name_ main
parser = argparse.ArgumentParser (
prog="ImgRar v1.0",
description="Convert small-Medium codes to Images And Vice-Versa",

8
0

)

parser.add_argument("-output", "--output", help="Set Output Directory")
parser.add_argument("-input", Input", help="Set Input Directory")
parser.add_argument (
“-codeZpng", "--Code2Png", help="Convert From Code to Png Image”
)
1 parser.add_argument (
18 =png2Gode", "--Png2Code", help="Convert From Png Image to Code"

19 )

20 parser.add_argument(" hel

“--Flag" “Binary Standard")

22 print (parser .prog)

23 print (parser.description)

24

25 # parse the arguments

26 args = parser.parse_args()

id obj = convert(args.Input, args.Output)

objbase = baseconversion(args.Input, args.Output)

if args.Flag == "True"

if args.Code2Png is not None:
objbase.code2png()

if args.Png2Code is not None:
objbase. png2code ()

35 else:
36 if, args.Code2Png is not None:
37 obj .code2png ()

38 if, args.Png2Code is not None:

39 obj .png2code ()
