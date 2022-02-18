# beta version comparison photo - 0.1

import pyautogui
from PIL import Image
from PIL import Image, ImageChops

image_1=Image.open('1.png') # photo for comparison 1
image_2=Image.open('2.png') # photo for comparison 2

result=ImageChops.difference(image_1, image_2)
# result.show() opens two photos

if result.getbbox() != None:
	print("разные фото")

else:
	print('Одинаковые')

print(result.getbbox())
