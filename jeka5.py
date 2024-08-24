from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import webbrowser
import os
import win32api
import sys
wo = win32api.ShellExecute
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 361, 41))
        self.label.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.label.setIndent(5)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 461, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 120, 281, 151))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Bgit = QtWidgets.QPushButton(self.frame)
        self.Bgit.setGeometry(QtCore.QRect(0, 60, 91, 41))
        self.Bgit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bgit.setObjectName("Bgit")
        self.Bdoc = QtWidgets.QPushButton(self.frame)
        self.Bdoc.setGeometry(QtCore.QRect(0, 100, 91, 41))
        self.Bdoc.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bdoc.setObjectName("Bdoc")
        self.Bmus = QtWidgets.QPushButton(self.frame)
        self.Bmus.setGeometry(QtCore.QRect(90, 60, 91, 41))
        self.Bmus.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bmus.setObjectName("Bmus")
        self.Bvid = QtWidgets.QPushButton(self.frame)
        self.Bvid.setGeometry(QtCore.QRect(180, 60, 91, 41))
        self.Bvid.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bvid.setObjectName("Bvid")
        self.Bpic = QtWidgets.QPushButton(self.frame)
        self.Bpic.setGeometry(QtCore.QRect(180, 100, 91, 41))
        self.Bpic.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bpic.setObjectName("Bpic")
        self.Bdow = QtWidgets.QPushButton(self.frame)
        self.Bdow.setGeometry(QtCore.QRect(90, 100, 91, 41))
        self.Bdow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Bdow.setObjectName("Bdow")
        self.Beval = QtWidgets.QPushButton(self.frame)
        self.Beval.setGeometry(QtCore.QRect(0, 20, 91, 41))
        self.Beval.setObjectName("Beval")
        self.Btime = QtWidgets.QPushButton(self.frame)
        self.Btime.setGeometry(QtCore.QRect(180, 20, 91, 41))
        self.Btime.setObjectName("Btime")
        self.Bfind = QtWidgets.QPushButton(self.frame)
        self.Bfind.setGeometry(QtCore.QRect(90, 20, 91, 41))
        self.Bfind.setObjectName("Bfind")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 300, 21, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Downloads/ac5b6195662f71dd64db1bb94a6e87e2.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 340, 211, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/ac5b6195662f71dd64db1bb94a6e87e2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 290, 211, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/Png.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.lineEdit.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Beval.clicked.connect(self.button_eval)
        self.Bfind.clicked.connect(self.button_find)
        self.Btime.clicked.connect(self.button_time)
        self.Bgit.clicked.connect(self.button_github)
        self.Bmus.clicked.connect(self.button_music)
        self.Bvid.clicked.connect(self.button_video)
        self.Bdoc.clicked.connect(self.button_doc)
        self.Bdow.clicked.connect(self.button_dow)
        self.Bpic.clicked.connect(self.button_pic)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ответ Жеки"))
        self.Bgit.setText(_translate("MainWindow", "Github"))
        self.Bdoc.setText(_translate("MainWindow", "Документы"))
        self.Bmus.setText(_translate("MainWindow", "Музыка"))
        self.Bvid.setText(_translate("MainWindow", "Видео"))
        self.Bpic.setText(_translate("MainWindow", "Картинки"))
        self.Bdow.setText(_translate("MainWindow", "Загрузки"))
        self.Beval.setText(_translate("MainWindow", "посчитай"))
        self.Btime.setText(_translate("MainWindow", "время"))
        self.Bfind.setText(_translate("MainWindow", "найди"))

    def button_eval(self):
        self.label.setText(str(eval(self.lineEdit.text())))
    def button_find(self):
        webbrowser.open_new_tab("https://yandex.ru/search/?text=" + str(self.lineEdit.text()))
    def button_time(self):
        self.label.setText(f'{datetime.datetime.now()}')
    def button_github(self):
        wo(0, 'open', 'C:/Users/user/AppData/Local/GitHubDesktop/GitHubDesktop.exe', None, '.', 1)
    def button_music(self):
        wo(0, 'open', 'C:/Users/user/Music', None, '.', 1)
    def button_video(self):
        wo(0, 'open', 'C:/Users/user/Videos', None, '.', 1)
    def button_doc(self):
        wo(0, 'open', 'C:/Users/user/Documents', None, '.', 1)
    def button_dow(self):
        wo(0, 'open', 'C:/Users/user/Downloads', None, '.', 1)
    def button_pic(self):
        wo(0, 'open', 'C:/Users/user/Pictures', None, '.', 1)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

jeka = 'JEKA'
print(f'{jeka}, Здравствуй, {username}!')
while True:
    username = os.getlogin()
    enter = input(f'{username}: ')  # Ввод запроса
    task = enter[enter.find(' '):]
    something = enter.lower()