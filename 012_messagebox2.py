import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from first_ui import Ui_Dialog
class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.leName.setText("홍길동")
        self.pbConfirm.clicked.connect(self.confirmButton)

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

    def confirmButton(self):
        print(self.leName.text() + " 님 반갑습니다")
        ret = self.showMsgBox("파이썬 수업",
                        "수강 신청",
                        "파이썬 RPA 과목을 수강하시겠습니까?",
                        QMessageBox.Information,
                        QMessageBox.Ok | QMessageBox.Discard | QMessageBox.Cancel,
                        QMessageBox.Ok)

        if ret == QMessageBox.Ok:
            print("Yes 버튼 눌림")
        elif ret == QMessageBox.Cancel:
            print("No 버튼 눌림")
        else:
            print("Discard 버튼 눌림")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())