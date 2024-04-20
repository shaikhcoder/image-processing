# from PIL import Image,ImageFilter

# img = Image.open("./src/images/astro.jpg")
# # filterImage = img.filter(ImageFilter.SMOOTH)
# filterImage = img

# # filterImage = filterImage.rotate(180)
# filterImage.thumbnail((400,400))
# # box = (100,100,400,400)
# # filterImage = filterImage.crop(box)
# # filterImage.show()
# filterImage.save("grey.png")

import sys
import os
from PIL import Image

path = "./src/images/"
convertFolderName = "jpg_to_png"

if not os.path.exists(os.path.join(path,convertFolderName)):
    os.makedirs(os.path.join(path,convertFolderName))
folderJPGFiles = [i for i in os.listdir(path) if os.path.splitext(i)[1]]
for i in folderJPGFiles:
    img = Image.open(os.path.join(path,i))
    img.save(f"{os.path.join(path,convertFolderName,os.path.splitext(i)[0])}.png",'png')