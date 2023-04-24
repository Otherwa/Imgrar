pngquant.config(
#     _pngquant_,
#     min_quality=5,
#     max_quality=5,
# )

# for filename in os.listdir(_input_fol):
#     filepath = os.path.join(_input_fol, filename)
#     with open(filepath, "rb") as file:
#         code = file.read()

#     lexer = PythonLexer()
#     formatter = ImageFormatter(font_name="Courier New", font_size=16)
#     image_data = highlight(code, lexer, formatter)

#     with open(_output_fol + "\\" + filename + ".png", "wb") as file:
#         file.write(image_data)

#     for i in range(5):
#         print(".", end="")
#         sleep(0.2)

#     pngquant.quant_image(_output_fol + "\\" + filename + ".png")
#     print("\n" + filename + " ✅", end="\n")

#     sleep(1)
