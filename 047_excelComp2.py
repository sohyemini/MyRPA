import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from excelComp import Ui_Dialog
class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbOri.clicked.connect(self.pbOriClick)
        self.pbComp.clicked.connect(self.pbCompClick)
        self.pbOut.clicked.connect(self.pbOutClick)
        self.pbExec.clicked.connect(self.pbExecClick)
        self.pbQuit.clicked.connect(self.pbQuitClick)

        self.rbKey.clicked.connect(self.rbKeyClick)
        self.rbStatic.clicked.connect(self.rbStaticClick)

        self.rbStatic.click()
        print(self.rbStatic.isChecked())
        print(self.rbKey.isChecked())
    def pbOriClick(self):
        print("원본파일")
    def pbCompClick(self):
        print("비교파일")
    def pbOutClick(self):
        print("출력파일")
    def pbExecClick(self):
        print("실행")
    def pbQuitClick(self):
        print("종료")
    def rbKeyClick(self):
        print("구분코드")
    def rbStaticClick(self):
        print("고정포맷")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())