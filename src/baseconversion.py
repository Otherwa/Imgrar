from PIL import Image
import os
import math
from time import sleep


def convert_to_grid(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append((i, number // i))

    print(factors)
    rows, columns = factors[-1]  # Get the factors closest together
    return rows, columns


def add_white_spaces(num_str):
    num_len = len(num_str)
    if num_len % 10 != 0:
        white_spaces = bytes(" " * (10 - (num_len % 10)), "utf-8")
        num_str += white_spaces
    return num_str


class baseconversion:
    def __init__(self, inputfolder, outputfolder):
        self.infolder = inputfolder
        self.outfolder = outputfolder

        # make folder
        os.makedirs(self.outfolder, exist_ok=True)
        os.makedirs(self.infolder, exist_ok=True)

    def code2png(self):
        print("Code 2 Photo\n")
        for filename in os.listdir(self.infolder):
            filepath = os.path.join(self.infolder, filename)
            with open(filepath, "r") as f:
                data = f.read()
            binary_data = bytes(data, "utf-8")
            print(f"File Bytes : {len(binary_data)}")
            binary_data = add_white_spaces(binary_data)
            # add white space to adjust the rxc

            cols, rows = convert_to_grid(len(binary_data))
            img = Image.frombytes("L", (rows, cols), binary_data)
            print(f"Image dim : {img.size}")
            img.save(os.path.join(self.outfolder, filename) + ".png")
            print(filename + " ✅\n", end="\n")
            sleep(1)
        print("\nDone 🤖✅")

    def png2code(self):
        print("Photo 2 Code\n")
        for filename in os.listdir(self.outfolder):
            img = Image.open(os.path.join(self.outfolder, filename))
            binary_data = img.tobytes()
            text_data = binary_data.decode("utf-8")
            file = filename.split(".")
            file = file[0] + "." + file[1]
            with open(os.path.join(self.infolder, file), "w") as f:
                f.writelines(text_data)
            print(f"Image dim : {img.size}")
            print(filename + " ✅\n", end="\n")
