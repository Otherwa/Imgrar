import os
import argparse
from src.baseconversion import baseconversion
from src.imagetomp4 import ImageToVideoConverter
from src.imagetomp4 import VideoToImagesConverter  # Import the new class

# Create the argument parser
if __name__ == "__main__":
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
        "-imagetomp4",
        "--ImageToMp4",
        action="store_true",
        help="Convert a series of images to MP4 video",
    )
    parser.add_argument(
        "-mp42images",
        "--Mp42Images",
        action="store_true",
        help="Convert MP4 video to a series of images",
    )
    parser.add_argument(
        "-fsize",
        "--fsize",
        default="320*240",
        help="Frame size for Code to PNG conversion (default: 320*240)",
    )
    parser.add_argument(
        "-framerate",
        "--FrameRate",
        type=int,
        default=24,
        help="Frame rate for MP4 video",
    )
    parser.add_argument(
        "-framesize",
        "--FrameSize",
        default="640*480",
        help="Frame size for MP4 video (e.g., 640*480)",
    )
    parser.add_argument(
        "-frameinterval",
        "--FrameInterval",
        type=int,
        default=1,
        help="Interval for frames extracted from MP4 video (default: 1, means every frame)",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.Output, exist_ok=True)

    # Run Code2Png or Png2Code conversion if specified
    if args.Code2Png or args.Png2Code:
        frame_size = args.fsize if args.fsize else "320*240"
        objbase = baseconversion(args.Input, args.Output, frame_size)

        if args.Code2Png:
            objbase.code2png()
        if args.Png2Code:
            objbase.png2code()

    # Run Image to MP4 conversion if specified
    elif args.ImageToMp4:
        # Convert frame size from string to tuple
        frame_size = tuple(map(int, args.FrameSize.split("*")))

        # Initialize and run the ImageToVideoConverter
        converter = ImageToVideoConverter(
            input_folder=args.Input,
            output_folder=args.Output,
            video_filename="output_video.mp4",
            frame_rate=args.FrameRate,
            frame_size=frame_size,
        )
        converter.convert()

    # Run MP4 to images conversion if specified
    elif args.Mp42Images:
        video_file = os.path.join(args.Input)  # Assuming Input is the path to the video
        converter = VideoToImagesConverter(
            video_file, args.Output, frame_interval=args.FrameInterval
        )
        converter.convert()
    else:
        print(
            "Please specify a valid option: -code2png, -png2code, -imagetomp4, or -mp42images."
        )
