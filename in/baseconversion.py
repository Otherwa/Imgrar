from PIL import Image
import os
from time import sleep


def factors(n):
    factors = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            factors.append(i)
    return factors


class baseconversion:
    def __init__(self, inputfolder, outputfolder):
        self.infolder = inputfolder
        self.outfolder = outputfolder

        # make folder
        os.makedirs(self.outfolder, exist_ok=True)
        os.makedirs(self.infolder, exist_ok=True)

    def code2png(self):
        print("Code 2 png binary\n")
        for filename in os.listdir(self.infolder):
            filepath = os.path.join(self.infolder, filename)
            with open(filepath, "r") as f:
                data = f.read()
            binary_data = bytes(data, "utf-8")
            print(f"File Bytes : {len(binary_data)}")
            sizes = factors(len(binary_data))
            img = Image.frombytes(
                "L", (sizes[len(sizes) // 2 - 1], sizes[len(sizes) // 2]), binary_data
            )
            print(f"Image dim : {img.size}")
            img.save(os.path.join(self.outfolder, filename) + ".png")
            print(filename + " ✅\n", end="\n")
            sleep(1)
        print("\nDone 🤖✅")

    def png2code(self):
        print("Png 2 Code Binary")
        for filename in os.listdir(self.outfolder):
            filepath = os.path.join(self.outfolder, filename)
            img = Image.open(filepath)
            binary_data = img.tobytes()
            text_data = binary_data.decode("utf-8")
            file = filename.split(".")
            file = file[0] + "." + file[1]
            with open(os.path.join(self.infolder, file), "w") as f:
                f.writelines(text_data)
            print(f"Image dim : {img.size}")
            print(filename + " ✅\n", end="\n")
            print(filepath + " Done ✅")
  