# importing PIL Module
from PIL import Image

# open the original image
original_img = Image.open(r"C:\Users\RobotComp.ru\PycharmProjects\olympTask\image.png")

# Flip the original image vertically
vertical_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
vertical_img.save("new_image.png")

# close all our files object
original_img.close()
vertical_img.close()
