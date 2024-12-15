import os
import argparse
from .BaseConversion import Baseconversion


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        prog="ImgRar v1.0",
        description="Convert Small-Medium codes to Images and vice versa, or compile a series of images into an MP4 video.",
    )

    # Define the arguments
    parser.add_argument(
        "-output", "--Output", required=True, help="Set Output Directory"
    )
    parser.add_argument("-input", "--Input", required=True, help="Set Input Directory")
    parser.add_argument(
        "-code2png",
        "--Code2Png",
        action="store_true",
        help="Convert from Code to PNG Image",
    )
    parser.add_argument(
        "-png2code",
        "--Png2Code",
        action="store_true",
        help="Convert from PNG Image to Code",
    )
    parser.add_argument(
        "-fsize",
        "--fsize",
        default="320*240",
        help="Frame size for Code to PNG conversion (default: 320*240)",
    )


    # Parse the arguments
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.Output, exist_ok=True)

    # Run Code2Png or Png2Code conversion if specified
    if args.Code2Png or args.Png2Code:
        frame_size = args.fsize if args.fsize else "320*240"
        objbase = Baseconversion(args.Input, args.Output, frame_size)

        if args.Code2Png:
            objbase.code2png()
        if args.Png2Code:
            objbase.png2code()
