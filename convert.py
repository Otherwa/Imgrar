from src.conversion import convert
from src.baseconversion import baseconversion
import argparse

# create the argument parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ImgRar v1.0",
        description="Convert Small-Medium codes to Images And Vice-Versa",
    )

    parser.add_argument("-output", "--Output", help="Set Output Directory")
    parser.add_argument("-input", "--Input", help="Set Input Directory")
    parser.add_argument(
        "-code2png", "--Code2Png", help="Convert From Code to Png Image"
    )
    parser.add_argument(
        "-png2code", "--Png2Code", help="Convert From Png Image to Code"
    )
    parser.add_argument("-flag", "--Flag", help="Binary Standard")

    print(parser.prog)
    print(parser.description)

    # parse the arguments
    args = parser.parse_args()
    if args.Input and args.Output:
        obj = convert(args.Input, args.Output)
        objbase = baseconversion(args.Input, args.Output)

        if args.Flag == "True":
            if args.Code2Png is not None:
                objbase.code2png()
            if args.Png2Code is not None:
                objbase.png2code()
        else:
            if args.Code2Png is not None:
                obj.code2png()
            if args.Png2Code is not None:
                obj.png2code()
    else:
        print("convert.py -h or convert.py --help")
