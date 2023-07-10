import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from first_ui import Ui_Dialog
class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.leName.setText("홍길동")
        self.pbConfirm.clicked.connect(self.confirmButton)

    def confirmButton(self):
        print(self.leName.text() + " 님 반갑습니다")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())