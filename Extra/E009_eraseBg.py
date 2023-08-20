from rembg import remove
from PIL import Image

loaded_img = Image.open(r"..\files\cat.jpg")
out_img = remove(loaded_img)
out_img.save(r"..\files\nobg_cat.png")

loaded_img = Image.open(r"..\files\prague.jpg")
out_img = remove(loaded_img)
out_img.save(r"..\files\nobg_prague.png")

loaded_img = Image.open(r"..\files\lady.jpg")
out_img = remove(loaded_img)
out_img.save(r"..\files\nobg_lady.png")