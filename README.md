Here is the updated version of your `README.md` file with the corrected usage example reflecting the command-line tool name `imgrar-cli` and the updated argument formats.

```markdown
# ImgRar v1.1.0

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
| `--fsize`         | `-fsize`   | No       | Set the frame size for PNG conversion (default: `320x240`).                                |

### Example Commands
1. **Code to PNG Conversion:**
   ```bash
   imgrar-cli -input ".\test\in" -output ".\test\out\test1" --Code2Png --fsize 640x480
   ```
   Converts code files in `.\test\in` to PNG images, saving them to `.\test\out\test1` with a frame size of 640x480.

2. **PNG to Code Conversion:**
   ```bash
   imgrar-cli -input ".\test\in" -output ".\test\out\test1" --Png2Code
   ```
   Converts PNG images in `.\test\in` back into code files, saving them to `.\test\out\test1`.


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
For support or questions, email: [atharvdesai2002@gmail.com](mailto:atharvdesai2002@gmail.com).
```

### Key Updates:
1. **Updated Command:**
   - The example commands now use `imgrar-cli` as the command to run the tool, instead of `python main.py`.

2. **Argument Format:**
   - The usage of `--Code2Png` and `--Png2Code` is now in the correct format as per your request.

3. **Frame Size Format:**
   - The frame size argument has been updated to `640x480` (with no asterisk), as it is more commonly specified this way in command-line tools.
