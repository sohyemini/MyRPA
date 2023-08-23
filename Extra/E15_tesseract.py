from PIL import Image
import pytesseract

# English
print(pytesseract.image_to_string(Image.open(r'..\files\test.png')))
print("-------------------------------")
# Kor only
print(pytesseract.image_to_string(Image.open(r'..\files\test_kr.png'), lang='kor'))
print("-------------------------------")
print(pytesseract.image_to_string(Image.open(r'..\files\test_book_kr.jpg'), lang='kor'))
print("-------------------------------")
print(pytesseract.image_to_string(Image.open(r'..\files\test_plate_kr.PNG'), lang='kor'))

