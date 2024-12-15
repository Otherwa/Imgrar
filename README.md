# ImgRar v1.0

## Overview
ImgRar is a versatile command-line tool for:
- **Code to PNG Conversion:** Transforming codes (up to several kilobytes in size) into visually encoded PNG images.
- **PNG to Code Conversion:** Decoding PNG images back into their original codes.
- **MP4 Video Preparation:** Preparing PNG files for MP4 video creation (future functionality).

## Key Features
- **Seamless Conversion:** Effortlessly switch between code and PNG formats.
- **Customizable Frame Size:** Specify the frame size during code-to-PNG conversions for precise output.
- **Flexible Directories:** Define input and output directories for streamlined workflows.

## Requirements
- **Python Version:** Python 3.6 or higher.
- **Dependencies:**
  - Built-in libraries: `argparse`, `os`.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/ImgRar.git
   ```
2. **Navigate to the Directory:**
   ```bash
   cd ImgRar
   ```
3. **Install Required Dependencies:**
   If additional modules are needed, install them using `pip`.

## Usage
### Command-Line Arguments
Run the tool with these arguments:

| Argument          | Short Form | Required | Description                                                                                 |
|-------------------|------------|----------|---------------------------------------------------------------------------------------------|
| `--Output`        | `-output`  | Yes      | Directory to save the output files.                                                        |
| `--Input`         | `-input`   | Yes      | Directory containing input files to process.                                               |
| `--Code2Png`      | `-code2png`| No       | Enable code-to-PNG conversion mode.                                                        |
| `--Png2Code`      | `-png2code`| No       | Enable PNG-to-code conversion mode.                                                        |
| `--fsize`         | `-fsize`   | No       | Set the frame size for PNG conversion (default: `320*240`).                                 |

### Example Commands
1. **Code to PNG Conversion:**
   ```bash
   python main.py -input ./input_dir -output ./output_dir -code2png -fsize 640*480
   ```
   Converts code files in `input_dir` to PNG images, saving them to `output_dir` with a frame size of 640x480.

2. **PNG to Code Conversion:**
   ```bash
   python main.py -input ./input_dir -output ./output_dir -png2code
   ```
   Converts PNG images in `input_dir` back into code files, saving them to `output_dir`.

## Directory Structure
```
ImgRar/
|
├── BaseConversion.py  # Core logic for conversions.
├── main.py            # Application entry point.
├── README.md          # Documentation file.
├── input_dir/         # Example input directory (replace with your path).
├── output_dir/        # Example output directory (replace with your path).
```

## Notes
- **Implementation Details:** Ensure the `BaseConversion` class in `BaseConversion.py` includes both `code2png` and `png2code` methods.
- **Input Files:** Use appropriate input files for smooth processing.

## License
This project is licensed under the MIT License. Refer to the `LICENSE` file for more details.

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## Contact
For support or questions, email: [your-email@example.com](mailto:your-email@example.com).
