from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import webbrowser
import os
import win32api
import time
wo = win32api.ShellExecute
D = 0

class Ui_AlkoKnopka(object):
    def setupUi(self, AlkoKnopka):
        AlkoKnopka.setObjectName("AlkoKnopka")
        AlkoKnopka.resize(562, 541)
        self.centralwidget = QtWidgets.QWidget(AlkoKnopka)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 271, 41))
        self.label.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.label.setIndent(5)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 461, 61))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 310, 211, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/ac5b6195662f71dd64db1bb94a6e87e2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Wa = QtWidgets.QLabel(self.centralwidget)
        self.Wa.setGeometry(QtCore.QRect(350, 260, 211, 231))
        self.Wa.setText("")
        self.Wa.setPixmap(QtGui.QPixmap("../../Downloads/Png.png"))
        self.Wa.setScaledContents(True)
        self.Wa.setObjectName("Wa")
        self.Death = QtWidgets.QPushButton(self.centralwidget)
        self.Death.setGeometry(QtCore.QRect(410, 270, 21, 31))
        self.Death.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/ac5b6195662f71dd64db1bb94a6e87e2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Death.setIcon(icon)
        self.Death.setObjectName("Death")
        self.Death_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Death_2.setGeometry(QtCore.QRect(540, 460, 21, 31))
        self.Death_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/bk49nvv4gyngv8s5jr0c7t369npxzgzp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Death_2.setIcon(icon1)
        self.Death_2.setObjectName("Death_2")
        AlkoKnopka.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AlkoKnopka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 26))
        self.menubar.setObjectName("menubar")
        AlkoKnopka.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AlkoKnopka)
        self.statusbar.setObjectName("statusbar")
        AlkoKnopka.setStatusBar(self.statusbar)

        self.Beval.clicked.connect(self.button_eval)
        self.Bfind.clicked.connect(self.button_find)
        self.Btime.clicked.connect(self.button_time)
        self.Bgit.clicked.connect(self.button_github)
        self.Bmus.clicked.connect(self.button_music)
        self.Bvid.clicked.connect(self.button_video)
        self.Bdoc.clicked.connect(self.button_doc)
        self.Bdow.clicked.connect(self.button_dow)
        self.Bpic.clicked.connect(self.button_pic)
        self.Death.clicked.connect(self.button_death)
        self.Death_2.clicked.connect(self.button_alko)

        self.retranslateUi(AlkoKnopka)
        QtCore.QMetaObject.connectSlotsByName(AlkoKnopka)

    def retranslateUi(self, AlkoKnopka):
        _translate = QtCore.QCoreApplication.translate
        AlkoKnopka.setWindowTitle(_translate("AlkoKnopka", "MainWindow"))
        self.label.setText(_translate("AlkoKnopka", "Ответ Жеки"))
        self.lineEdit.setText(_translate("AlkoKnopka", ""))
        self.Bgit.setText(_translate("AlkoKnopka", "Github"))
        self.Bdoc.setText(_translate("AlkoKnopka", "Документы"))
        self.Bmus.setText(_translate("AlkoKnopka", "Музыка"))
        self.Bvid.setText(_translate("AlkoKnopka", "Видео"))
        self.Bpic.setText(_translate("AlkoKnopka", "Картинки"))
        self.Bdow.setText(_translate("AlkoKnopka", "Загрузки"))
        self.Beval.setText(_translate("AlkoKnopka", "Посчитай"))
        self.Btime.setText(_translate("AlkoKnopka", "Время"))
        self.Bfind.setText(_translate("AlkoKnopka", "Найди"))


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
    def button_death(self):
        self.label.setText('...')
        time.sleep(1)
        self.label.setText(' Но... я не хочу умирать!')
        #time.sleep(2)
        #self.label.setText('Нет! НЕТ! НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ!!!!')
        #time.sleep(1)
        #os.system('shutdown /r /t 1')
    def button_alko(self):
        self.Bgit.setText("Gitрub")
        self.Bdoc.setText("Окунменты")
        self.Bmus.setText("уыка")
        self.Bvid.setText("Виео")
        self.Bpic.setText("Катинки")
        self.Bdow.setText("Загрурги")
        self.Beval.setText("Покчиккай")
        self.Btime.setText("Вермя")
        self.Bfind.setText("Нади")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlkoKnopka = QtWidgets.QMainWindow()
    ui = Ui_AlkoKnopka()
    ui.setupUi(AlkoKnopka)
    AlkoKnopka.show()
    sys.exit(app.exec_())

jeka = 'JEKA'
print(f'{jeka}, Здравствуй, {username}!')
while True:
    username = os.getlogin()
    enter = input(f'{username}: ')
    task = enter[enter.find(' '):]
    something = enter.lower()
