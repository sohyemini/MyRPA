import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from newsMailerUI import Ui_dlgMain
class MainWindow(QMainWindow, Ui_dlgMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())