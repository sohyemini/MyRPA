import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
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
        fname = self.fileOpenAndSave("원본파일선택")
        self.leOri.setText(fname)
        print(f"원본파일 : {fname}")
    def pbCompClick(self):
        fname = self.fileOpenAndSave("비교파일선택")
        self.leComp.setText(fname)
        print(f"비교파일 : {fname}")
    def pbOutClick(self):
        fname = self.fileOpenAndSave("저장할 파일명 지정", False)
        self.leOut.setText(fname)
        print(f"출력파일 : {fname}")
    def pbExecClick(self):
        print("실행")
    def pbQuitClick(self):
        print("종료")
    def rbKeyClick(self):
        print("구분코드")
    def rbStaticClick(self):
        print("고정포맷")

    def fileOpenAndSave(self, str, open=True):
        filter = "All files(*.xlsx : *.xls) ;; Excel 통합 문서(*.xlsx) ;; " \
                 "Excel 97 - Excel 2003 통합 문서(*.xls)"
        if open:
            fname = QFileDialog.getOpenFileName(self, str, '.\\', filter)
        else:
            fname = QFileDialog.getSaveFileName(self, str, '.\\', filter)

        print(type(fname))
        print(os.path.dirname(fname[0]))
        return fname[0]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())