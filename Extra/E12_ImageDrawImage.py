from PIL import Image, ImageDraw

MainImg = Image.open(r'..\files\lady.jpg')
yes_img = Image.open(r'..\res\yes24A.png')
no_img = Image.open(r'..\res\no24A.png')

ex = MainImg.width
ey = MainImg.height

newImg = Image.new(mode='RGB', size=(ex+100, ey+100))
drawNew = ImageDraw.Draw(newImg, 'RGB')
boxColor = (50, 50, 50)
drawNew.rectangle((0, 0, newImg.width, newImg.height), fill=boxColor)
# newImg.show()

MainImg.paste(yes_img, (100, 100))
MainImg.paste(no_img, (100, ey - 100))
# MainImg.show()
draw = ImageDraw.Draw(MainImg, 'RGB')

lineThick = 10
lineColor = (255, 20, 20)
boxColor = (24, 255, 24)
draw.rectangle((200, 200, ex-200, ey-200), outline=boxColor, width=lineThick)
draw.line((200, 200, ex-200, ey-200), fill=lineColor ,width=lineThick)

newImg.paste(MainImg, (50, 50))

newImg.show()
newImg.save(r'..\files\lady_draw.jpg')
