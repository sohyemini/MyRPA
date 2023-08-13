import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QLabel

from PySide6.QtGui import Qt, QPixmap

from newsMailerUI import Ui_dlgMain
from newsMailerDB import DBase
class MainWindow(QMainWindow, Ui_dlgMain):

    dbase = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbase = DBase()

        self.tblNews.cellClicked.connect(self.newsTableClicked)

        self.initNewsTable()
        self.loadNewsTable()
        self.initEmailTable()
        # self.loadEmailTable()

    def initNewsTable(self):
        self.tblNews.setSelectionBehavior(QAbstractItemView.SelectRows) # 열 선택
        self.tblNews.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 수정금지
        self.tblNews.setColumnCount(3)
        self.tblNews.setHorizontalHeaderLabels(["No", "Keyword", "send"])
        self.tblNews.setColumnWidth(0, 30)
        self.tblNews.setColumnWidth(1, 200)
        self.tblNews.setColumnWidth(2, 40)

    def initEmailTable(self):
        self.tblEmail.setSelectionBehavior(QAbstractItemView.SelectRows) # 열 선택
        self.tblEmail.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 수정금지
        self.tblEmail.setColumnCount(5)
        self.tblEmail.setHorizontalHeaderLabels(["No", "KIDX", "Name", "Email", "Memo"])
        self.tblEmail.setColumnWidth(0, 30)
        self.tblEmail.setColumnWidth(1, 40)
        self.tblEmail.setColumnWidth(2, 80)
        self.tblEmail.setColumnWidth(3, 120)
        self.tblEmail.setColumnWidth(4, 40)

    def loadNewsTable(self):
        rows = self.dbase.getAllData('keyword')
        cnt = len(rows)
        self.tblNews.setRowCount(cnt)

        for i in range(cnt):
            idx, keyword, send = rows[i]
            idx_item = QTableWidgetItem(str(idx))
            idx_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tblNews.setItem(i, 0, idx_item)
            self.tblNews.setItem(i, 1, QTableWidgetItem(keyword))

            if send == 1:
                iconSrc = QPixmap('./res/yes24A.png')
            else:
                iconSrc = QPixmap('./res/no24A.png')
            licon = QLabel()
            licon.setPixmap(iconSrc)
            licon.setAlignment(Qt.AlignCenter)
            self.tblNews.setCellWidget(i, 2, licon)

    def loadEmailTable(self, kidx):
        rows = self.dbase.getEmailForSending(kidx)
        cnt = len(rows)
        self.tblEmail.setRowCount(cnt)

        for i in range(cnt):
            idx, kidx, name, email, memo = rows[i]
            idx_item = QTableWidgetItem(str(idx))
            idx_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tblEmail.setItem(i, 0, idx_item)

            kidx_item = QTableWidgetItem(str(kidx))
            kidx_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tblEmail.setItem(i, 1, kidx_item)

            name_item = QTableWidgetItem(str(name))
            name_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tblEmail.setItem(i, 2, name_item)

            self.tblEmail.setItem(i, 3, QTableWidgetItem(str(email)))
            self.tblEmail.setItem(i, 4, QTableWidgetItem(str(memo)))


    def newsTableClicked(self, row, col):
        print(self.tblNews.item(row, 0).text())
        self.loadEmailTable(int(self.tblNews.item(row, 0).text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())