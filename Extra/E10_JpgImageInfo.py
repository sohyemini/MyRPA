import os
from PIL import Image
class ImageInfo():
    def setJpgImage(self, filename):
        _image = Image.open(filename)
        self._filename = filename
        self._format = _image.format
        self._mode = _image.mode
        self._width = _image.width
        self._height = _image.height
        try:
            self._dpi1, self._dpi2 = _image.info.get('dpi')
        except:
            self._dpi1 = 70
            self._dpi2 = 70
        self._widthCm = format((self._width / self._dpi1 ) *2.54, '.2f')
        self._heightCm = (self._height / self._dpi1 ) *2.54

        self.printImageInformation()

    def setPngImage(self, filename):
        _image = Image.open(filename)
        self._filename = filename
        self._format = _image.format
        self._mode = _image.mode
        self._width = _image.width
        self._height = _image.height
        try:
            self._dpi1, self._dpi2 = _image.info.get('dpi')
        except:
            self._dpi1 = 70
            self._dpi2 = 70
        self._widthCm = round((self._width / self._dpi1)*2.54, 3)
        self._heightCm = round((self._height / self._dpi1)*2.54, 3)
        self._widthCm = (self._width / self._dpi1) * 2.54
        self._heightCm = (self._height / self._dpi1) * 2.54

        self.printImageInformation()

    def printImageInformation(self):
        print(f"=============================================")
        print(f"이미지 파일 이름 : {self._filename}")
        print(f"이미지 파일 형식(format) : {self._format}")
        print(f"이미지 색상모드 : {self._mode}")
        print(f"이미지 너비(pixel): {self._width}")
        print(f"이미지 높이(pixel) : {self._height}")
        print(f"이미지 DPI : {self._dpi1}")
        print(f"이미지 너비(cm): {self._widthCm}")
        print(f"이미지 높이(cm): {self._heightCm}\n")

    def readImage(self, fname):
        # 파일의 존재 여부 확인
        if False == os.path.isfile(fname):
            print(f"{fname}이 존재하지 않습니다.")
            return

        # 파일명과 확장자 분리
        filename, ext = os.path.splitext(fname)

        if ext == '.png' or ext == '.PNG':
            print(f"=============================================")
            print("PNG 파일이 입력되었습니다")
            self.setPngImage(fname)
        elif ext == '.jpg' or ext == '.JPG':
            print(f"=============================================")
            print("JPG 파일이 입력되었습니다")
            self.setJpgImage(fname)
        else:
            print(f"\n{ext} 형식의 파일은 지원하지 않습니다")

if __name__ == "__main__":
    II = ImageInfo()
    II.readImage(r'..\files\cat.jpg')
    II.readImage(r'..\files\nobg_lady.png')