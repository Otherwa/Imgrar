from src.convertion import convert
import argparse

# create the argument parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ImgRar v1.0",
        description="Convert Small-Medium codes to Images And Vice-Versa",
    )

    parser.add_argument("-output", "--Output", help="Set Output Directory")
    parser.add_argument("-input", "--Input", help="Set Input Directory")
    parser.add_argument("-intp", "--Intp", help="Set Png Quantnt Interpreter Path")

    print(parser.prog)
    print(parser.description)

    # parse the arguments
    args = parser.parse_args()

    if args.Input and args.Output and args.Intp:
        obj = convert(args.Input, args.Output, args.Intp)
        obj.code2png()
    elif args.Input and args.Output and args.Intp:
        print("covert.py -h or convert.py --help for usage")
    else:
        (":print")
