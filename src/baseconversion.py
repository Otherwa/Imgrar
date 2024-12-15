from datetime import datetime
from PIL import Image
import os
import math
from time import sleep
import json
import numpy as np


def convert_to_grid(number):
    # Find factors to determine the grid size for the image
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    rows, columns = factors[-1]  # Get the factors closest together
    return rows, columns


def add_white_spaces(num_str, frame_size: int):
    # Add white space to the binary string to fit the frame size
    num_len = len(num_str)
    if num_len % frame_size != 0:
        white_spaces = bytes("\u0020" * (frame_size - (num_len % frame_size)), "utf-8")
        num_str += white_spaces
    return num_str


class Baseconversion:
    def __init__(self, inputfolder, outputfolder, frame_size="320 * 240"):
        self.infolder = inputfolder
        self.outfolder = outputfolder
        self.frame_size = int(eval(frame_size))  # Validate or handle eval properly
        os.makedirs(self.outfolder, exist_ok=True)
        os.makedirs(self.infolder, exist_ok=True)

        self.files = []

    def code2png(self):
        print("Code 2 Photo\n")
        for filename in os.listdir(self.infolder):
            filepath = os.path.join(self.infolder, filename)

            # Check if file exists before opening
            if not os.path.isfile(filepath):
                print(f"Skipping {filename}, it is not a valid file.")
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = f.read()
                binary_data = bytes(data, "utf-8")
                print(f"File Bytes: {len(binary_data)}")

                binary_data = add_white_spaces(binary_data, self.frame_size)
                cols, rows = convert_to_grid(len(binary_data))

                # Create image from the binary data
                img = Image.new("L", (rows, cols))
                img.putdata(list(binary_data))  # Store the data in the image

                # Metadata
                data = self.fileDetails(filepath)
                data["size"] = img.size
                self.files.append(data)

                img.save(os.path.join(self.outfolder, filename) + ".png")
                print(f"{filename} ✅\n", end="\n")

                sleep(1)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

        # Save metadata as JSON
        files_json = json.dumps(self.files, indent=4)
        with open(os.path.join(self.outfolder, "metadata.json"), "w") as writer:
            writer.write(files_json)

        print("\nDone 🤖✅")

    def fileDetails(self, filename):
        # Get file metadata
        file_path = os.path.join(filename)
        file_size = os.path.getsize(file_path)
        creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
        modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        file_info = {
            "file_name": filename,
            "file_path": file_path,
            "file_size": file_size,
            "creation_time": str(creation_time),
            "modification_time": str(modification_time),
        }
        print(file_info)
        return file_info

    def png2code(self):
        print("Photo 2 Code\n")
        for filename in os.listdir(self.outfolder):
            if not filename.endswith(".png"):
                continue

            try:
                img = Image.open(os.path.join(self.outfolder, filename))

                # Convert image data back to bytes
                binary_data = np.array(img).tobytes()
                text_data = binary_data.decode("utf-8")

                # Remove extension and save to the original input folder
                file_name_no_ext = os.path.splitext(filename)[0]
                output_path = os.path.join(self.infolder, file_name_no_ext)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text_data)

                print(f"Image dim: {img.size}")
                print(f"{filename} ✅\n", end="\n")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
