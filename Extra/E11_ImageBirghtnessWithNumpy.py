from PIL import Image
import numpy as np

img = Image.open(r'..\files\lady.jpg')
img.show()
print(img.width, img.height)

img_arr1 = np.array(img)
img_arr2 = np.array(img)
print(img_arr1)
print(img_arr1.shape[0], img_arr1.shape[1], img_arr1.shape[2])

for i in range(img_arr1.shape[0]):
    for j in range(img_arr1.shape[1]):
        for k in range(img_arr1.shape[2]):
            l = img_arr1[i][j][k]
            l = l + 100
            # if l > 255:
            #     l = 255
            img_arr1[i][j][k] = l

bright_img = Image.fromarray(img_arr1)
bright_img.show()
bright_img.save(r'..\files\lady_bright.jpg')

for i in range(img_arr2.shape[0]):
    for j in range(img_arr2.shape[1]):
        for k in range(img_arr2.shape[2]):
            l = img_arr2[i][j][k]
            l = l - 100
            # if l < 0:
            #      l = 0
            img_arr2[i][j][k] = l

dark_img = Image.fromarray(img_arr2)
dark_img.show()
dark_img.save(r'..\files\lady_dark.jpg')
