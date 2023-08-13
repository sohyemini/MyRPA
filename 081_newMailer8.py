import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QLabel, QMessageBox
from PySide6.QtGui import Qt, QPixmap

from newsMailerUI import Ui_dlgMain
from newsMailerDB2 import DBase
class MainWindow(QMainWindow, Ui_dlgMain):

    dbase = None

    NONE = 0
    NEW  = 1
    EDIT = 2
    keywordMode = NONE

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbase = DBase()

        self.tblNews.cellClicked.connect(self.newsTableClicked)
        self.tblEmail.cellClicked.connect(self.emailTableClicked)
        self.pbNew.clicked.connect(self.pbNewClicked)
        self.pbCancel.clicked.connect(self.pbCancelClicked)
        self.pbSave.clicked.connect(self.pbSaveClicked)
        self.leNewID.setDisabled(True)
        self.leEmailID.setDisabled(True)

        self.initNewsTable()
        self.loadNewsTable()
        self.initEmailTable()

        self.tblNews.selectRow(0)
        self.newsTableClicked(0,0)
        self.tblNews.setFocus()
        self.tblEmail.selectRow(0)
        self.emailTableClicked(0,0)

        self.NewsDetailWidget(False)
        self.EmailDetailWidget(False)
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
        key = int(self.tblNews.item(row, 0).text())
        # print(self.tblNews.item(row, 0).text())
        self.loadEmailTable(key)
        row = self.dbase.getOneData('keyword', key)
        if row:
            idx, keyword, send = row[0]
            self.leNewID.setText(str(idx))
            self.leSearch.setText(keyword)
            if send == 1:
                self.cbSend.setChecked(True)
            else:
                self.cbSend.setChecked(False)

            self.leEmailID.clear()
            self.leName.clear()
            self.leEmail.clear()
            self.leMemo.clear()
            self.emailTableClicked(0, 0)
            self.pbEdit.setEnabled(True)
            self.pbDelete.setEnabled(True)
        else:
            self.pbEdit.setEnabled(False)
            self.pbDelete.setEnabled(False)

        self.pbNew.setEnabled(True)
        self.pbCancel.setEnabled(False)
        self.pbSave.setEnabled(False)

    def emailTableClicked(self, row, col):
        key = int(self.tblEmail.item(row, 0).text())
        row = self.dbase.getOneData('email', key)
        if row:
            idx, kidx, name, email, memo = row[0]
            self.leEmailID.setText(str(idx))
            self.leName.setText(name)
            self.leEmail.setText(email)
            self.leMemo.setText(memo)

            self.pbEditEmail.setEnabled(True)
            self.pbDeleteEmail.setEnabled(True)
        else:
            self.pbEditEmail.setEnabled(False)
            self.pbDeleteEmail.setEnabled(False)

        self.pbNewEmail.setEnabled(True)
        self.pbCancelEmail.setEnabled(False)
        self.pbSaveEmail.setEnabled(False)

    def NewsDetailWidget(self, enabled):
        self.leSearch.setEnabled(enabled)
        self.cbSend.setEnabled(enabled)

    def EmailDetailWidget(self, enabled):
        self.leEmailID.setEnabled(enabled)
        self.leName.setEnabled(enabled)
        self.leEmail.setEnabled(enabled)
        self.leMemo.setEnabled(enabled)

    def pbNewClicked(self):
        self.keywordMode = self.NEW

        self.leSearch.clear()
        self.leNewID.clear()
        self.cbSend.setChecked(False)

        self.pbNew.setEnabled(False)
        self.pbEdit.setEnabled(False)
        self.pbDelete.setEnabled(False)
        self.pbSave.setEnabled(True)
        self.pbCancel.setEnabled(True)

        self.leSearch.setEnabled(True)
        self.cbSend.setEnabled(True)

    def pbCancelClicked(self):
        ...

    def pbSaveClicked(self):
        if self.keywordMode == self.NEW:
            keyword = self.leSearch.text()
            if len(keyword) < 3:
                self.showMsgBox("키워드 추가",
                                "검색어 길이",
                                "검색어가 입력되지 않았거나 너무 짧습니다. 다시 입력해주세요",
                                QMessageBox.Information,
                                QMessageBox.Ok,
                                QMessageBox.Ok)
                return
            if self.cbSend.isChecked():
                send = 1
            else:
                send = 0
            self.dbase.insertKeyword(keyword, send)
            self.NewsDetailWidget(False)

            self.pbNew.setEnabled(True)
            self.pbEdit.setEnabled(True)
            self.pbDelete.setEnabled(True)
            self.pbSave.setEnabled(False)
            self.pbCancel.setEnabled(False)

            self.keywordMode = self.NONE
        elif self.keywordMode == self.EDIT:
            pass

    def showMsgBox(self, wndTitle, title, info, icon, btns, dbtn):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(wndTitle)
        msgbox.setText(title)
        msgbox.setInformativeText(info)
        msgbox.setIcon(icon)
        msgbox.setStandardButtons(btns)
        msgbox.setDefaultButton(dbtn)

        return msgbox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())