import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from excelComp import Ui_Dialog
from excelCompLib5 import StaticFormExcelCompare
from excelKeyCompLib3 import UniqueKeyExcelCompare
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

    # from 012_messagebox2.py ################################
    def showMsgBox(self, wndTitle, title, info, icon, btns, dbtn):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(wndTitle)
        msgbox.setText(title)
        msgbox.setInformativeText(info)
        msgbox.setIcon(icon)
        msgbox.setStandardButtons(btns)
        msgbox.setDefaultButton(dbtn)

        # QMessageBox.Ok, Cancel, Discard
        return msgbox.exec()

    ########################################################

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
        if len(self.leOri.text()) < 5 or len(self.leComp.text()) < 5 or len(self.leOut.text()) < 5:
            self.showMsgBox("에러",
                            "파일 입력 오류",
                            "파일이 모두 선택되거나 입력되지 않았습니다.",
                            QMessageBox.Warning,
                            QMessageBox.Ok | QMessageBox.Cancel,
                            QMessageBox.Ok)

            return

        if self.rbKey.isChecked():
            a = UniqueKeyExcelCompare()
        else:
            a = StaticFormExcelCompare()

        # a.setColor('123456', '789ABC', 'DEF123')
        a.setFiles(self.leOri.text(), self.leComp.text(), self.leOut.text())
        ret = a.run()
        if ret == a.SUCCESS:
            self.showMsgBox("완료",
                            "파일 비교 완료",
                            f"파일 비교가 정상적으로 완료되었습니다.\n{self.leOut.text()}",
                            QMessageBox.Information,
                            QMessageBox.Ok,
                            QMessageBox.Ok)
        elif ret == a.KEY_ERROR:
            self.showMsgBox("Error",
                            "구분코드 파일 비교",
                            f"중복되는 키가 있습니다. 각 파일의 중복 Key를 확인해주세요.",
                            QMessageBox.Critical,
                            QMessageBox.Ok,
                            QMessageBox.Ok)
        elif ret == a.SIZE_DIFFERENT:
            self.showMsgBox("Error",
                            "고정포맷 파일 비교",
                            f"행과 열의 크기가 다릅니다. 잘못된 부분이 없는지 확인해 주세요.",
                            QMessageBox.Critical,
                            QMessageBox.Ok,
                            QMessageBox.Ok)
        elif ret == a.FILE_OPEND:
            self.showMsgBox("Error",
                            "파일 쓰기 에러",
                            f"출력할 파일과 동일한 파일이 열려 있는 것 같습니다.",
                            QMessageBox.Critical,
                            QMessageBox.Ok,
                            QMessageBox.Ok)
    def pbQuitClick(self):
        exit(0)
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

        # print(fname)
        return fname[0]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())