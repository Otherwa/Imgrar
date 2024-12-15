ImgRar v1.0

Overview

ImgRar is a command-line tool designed for:

Converting small-to-medium codes into PNG images.

Converting PNG images back into their original codes.

Preparing PNG files to create MP4 videos (future functionality can be added).

Features

Code to PNG Conversion: Transform your codes into visually encoded PNG images.

PNG to Code Conversion: Extract and decode codes stored in PNG images.

Custom Frame Size: Set a frame size for PNG images during the conversion process.

Input and Output Directories: Specify directories for input files and saving output results.

Requirements

Python 3.6+

Required libraries:

argparse

os

Installation

Clone the repository:

git clone <https://github.com/your-repo/ImgRar.git>

Navigate to the project directory:

cd ImgRar

Install dependencies (if any additional modules are required).

Usage

Command-Line Arguments

Run the script with the following arguments:

Argument

Short Form

Required

Description

--Output

-output

Yes

Directory to save the output files.

--Input

-input

Yes

Directory containing input files to process.

--Code2Png

-code2png

No

Enable code-to-PNG conversion mode.

--Png2Code

-png2code

No

Enable PNG-to-code conversion mode.

--fsize

-fsize

No

Set the frame size for PNG conversion (default: 320*240).

Example Commands

Code to PNG Conversion:

python main.py -input ./input_dir -output ./output_dir -code2png -fsize 640*480

Converts code files in input_dir to PNG images, saving them to output_dir with a frame size of 640x480.

PNG to Code Conversion:

python main.py -input ./input_dir -output ./output_dir -png2code

Converts PNG images in input_dir back into code files, saving them to output_dir.

Directory Structure

ImgRar/
|
├── BaseConversion.py  # Contains the core logic for conversions.
├── main.py            # Entry point for the application.
├── README.md          # Documentation file.
├── input_dir/         # Example input directory (replace with your path).
├── output_dir/        # Example output directory (replace with your path).

Notes

Ensure the BaseConversion class is implemented in BaseConversion.py with the code2png and png2code methods.

Use valid input files for conversion.

License

This project is licensed under the MIT License. See LICENSE for more details.

Contribution

Contributions are welcome! Feel free to fork the project and submit a pull request.

Contact

For questions or issues, contact: <atharvdesai2002@gmail.com>.
