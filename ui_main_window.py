# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowrRtRCq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setMaximumSize(QSize(450, 500))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 461, 501))
        self.widget.setAutoFillBackground(False)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 5, 441, 490))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(
"border-image:url(./images/bg.png);"
"border-radius:20px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 20, 341, 51))
        font = QFont()
        font.setFamily(u"Bungee Inline")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 80, 411, 321))
        self.widget_2.setStyleSheet(u"")
        self.labelPicto = QLabel(self.widget_2)
        self.labelPicto.setObjectName(u"labelPicto")
        self.labelPicto.setEnabled(True)
        self.labelPicto.setGeometry(QRect(90, 10, 101, 91))
        self.labelPicto.setStyleSheet("border-image:url(./images/01d.png)")
        self.labelPicto.setFrameShape(QFrame.NoFrame)
        self.labelPicto.setFrameShadow(QFrame.Plain)
        self.labelTemp = QLabel(self.widget_2)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setGeometry(QRect(270, 10, 47, 13))
        font1 = QFont()
        font1.setFamily(u"Bungee Inline")
        font1.setPointSize(12)
        self.labelTemp.setFont(font1)
        self.labelCity = QLabel(self.widget_2)
        self.labelCity.setObjectName(u"labelCity")
        self.labelCity.setGeometry(QRect(20, 110, 381, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelCity.sizePolicy().hasHeightForWidth())
        self.labelCity.setSizePolicy(sizePolicy1)
        self.labelCity.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Bungee Inline")
        font2.setPointSize(14)
        self.labelCity.setFont(font2)
        self.labelCity.setLayoutDirection(Qt.LeftToRight)
        self.labelCity.setFrameShape(QFrame.NoFrame)
        self.labelCity.setLineWidth(1)
        self.labelCity.setMidLineWidth(0)
        self.labelCity.setScaledContents(False)
        self.labelCity.setAlignment(Qt.AlignCenter)
        self.labelCity.setWordWrap(False)
        self.labelTempMin = QLabel(self.widget_2)
        self.labelTempMin.setObjectName(u"labelTempMin")
        self.labelTempMin.setGeometry(QRect(310, 50, 47, 13))
        self.labelTempMin.setFont(font1)
        self.labelTempMin.setStyleSheet(u"color:rgb(189, 209, 255)")
        self.labelTempMax = QLabel(self.widget_2)
        self.labelTempMax.setObjectName(u"labelTempMax")
        self.labelTempMax.setGeometry(QRect(310, 70, 47, 13))
        self.labelTempMax.setFont(font1)
        self.labelTempMax.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.labelTemp_2N = QLabel(self.widget_2)
        self.labelTemp_2N.setObjectName(u"labelTemp_2N")
        self.labelTemp_2N.setGeometry(QRect(240, 50, 47, 13))
        self.labelTemp_2N.setFont(font1)
        self.labelTemp_3N = QLabel(self.widget_2)
        self.labelTemp_3N.setObjectName(u"labelTemp_3N")
        self.labelTemp_3N.setGeometry(QRect(240, 70, 47, 13))
        self.labelTemp_3N.setFont(font1)
        self.labelFeelLikeN = QLabel(self.widget_2)
        self.labelFeelLikeN.setObjectName(u"labelFeelLikeN")
        self.labelFeelLikeN.setGeometry(QRect(90, 220, 91, 16))
        self.labelFeelLikeN.setFont(font1)
        self.labelTempFeel = QLabel(self.widget_2)
        self.labelTempFeel.setObjectName(u"labelTempFeel")
        self.labelTempFeel.setGeometry(QRect(270, 220, 47, 13))
        self.labelTempFeel.setFont(font1)
        self.labelTempFeel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelHumidityPer = QLabel(self.widget_2)
        self.labelHumidityPer.setObjectName(u"labelHumidityPer")
        self.labelHumidityPer.setGeometry(QRect(270, 250, 47, 13))
        self.labelHumidityPer.setFont(font1)
        self.labelHumidityPer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelHumidityN = QLabel(self.widget_2)
        self.labelHumidityN.setObjectName(u"labelHumidityN")
        self.labelHumidityN.setGeometry(QRect(90, 250, 151, 16))
        self.labelHumidityN.setFont(font1)
        self.labelWindN = QLabel(self.widget_2)
        self.labelWindN.setObjectName(u"labelWindN")
        self.labelWindN.setGeometry(QRect(90, 280, 151, 16))
        self.labelWindN.setFont(font1)
        self.labelWindSpeed = QLabel(self.widget_2)
        self.labelWindSpeed.setObjectName(u"labelWindSpeed")
        self.labelWindSpeed.setGeometry(QRect(250, 280, 71, 16))
        self.labelWindSpeed.setFont(font1)
        self.labelWindSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelDescript = QLabel(self.widget_2)
        self.labelDescript.setObjectName(u"labelDescript")
        self.labelDescript.setGeometry(QRect(70, 160, 281, 51))
        font3 = QFont()
        font3.setFamily(u"Bungee Inline")
        font3.setPointSize(8)
        self.labelDescript.setFont(font3)
        self.labelDescript.setLayoutDirection(Qt.LeftToRight)
        self.labelDescript.setStyleSheet(u"color:rgb(255,255,255)")
        self.labelDescript.setAlignment(Qt.AlignCenter)
        self.button1 = QPushButton(self.widget)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(180, 450, 101, 31))
        self.button1.setStyleSheet(u":hover{background-color:rgb(11,220,255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:black;\n"
"border-radius:2px;\n"
"color:rgb(0,76,75);}\n"
"\n"
":pressed{background-color:rgb(5,191,255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:rgb(255,200,198);\n"
"border-radius:2px;\n"
"color:white;}")
        self.button1.setCheckable(False)
        self.button1.setFlat(True)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 410, 291, 31))
        font4 = QFont()
        font4.setFamily(u"Bungee Inline")
        font4.setPointSize(11)
        font4.setItalic(False)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-botttom:7px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button1.clicked.connect(on_click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"JL75TJ - Id\u0151j\u00e1r\u00e1s", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"JL75TJ - Id\u0151j\u00e1r\u00e1s", None))
        self.labelPicto.setText("")
        self.labelTemp.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.labelCity.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.labelTempMin.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.labelTempMax.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.labelTemp_2N.setText(QCoreApplication.translate("MainWindow", u"MIN:", None))
        self.labelTemp_3N.setText(QCoreApplication.translate("MainWindow", u"MAX:", None))
        self.labelFeelLikeN.setText(QCoreApplication.translate("MainWindow", u"H\u0151\u00e9rzet:", None))
        self.labelTempFeel.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.labelHumidityPer.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.labelHumidityN.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ratartalom:", None))
        self.labelWindN.setText(QCoreApplication.translate("MainWindow", u"SZ\u00e9l:", None))
        self.labelWindSpeed.setText(QCoreApplication.translate("MainWindow", u"0 Km/H", None))
        self.labelDescript.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"Friss\u00edt\u00e9s", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"V\u00e1ros n\u00e9v (pl.: Budapest)", None))
    # retranslateUi



##Internet elérés tesztelése
def check_internet(self):
    url = "http://www.openweathermap.org"
    timeout = 1
    answer = 0
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        answer = 1
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        answer = 0
    return answer

def getWeather(cityT):
     try:
      city = cityT
      lang='hu'
      api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=bb0fb32f8042c733a2b0d29c58c8e2b6&lang=" + lang
      json_data = requests.get(api).json()
      condition = json_data['weather'][0]['description']
      icon = json_data['weather'][0]['icon']
      temp = int(json_data['main']['temp']-273.15)
      tempMin = int(json_data['main']['temp_min']-273.15)
      tempMax = int(json_data['main']['temp_max'] - 273.15)
      tempFL = int(json_data['main']['feels_like'] - 273.15)
      humidity = int(json_data['main']['humidity'])
      windS = int(json_data['wind']['speed'])
      arrayD = [str(temp)+'°C', condition, icon, str(tempMin)+'°C', str(tempMax)+'°C', str(tempFL)+'°C', str(humidity)+'%', str(windS)+'km/h']
      print(arrayD)
      return arrayD
     except:
      print("Hiba! Kérem ellenőrizze a megadott település nevet!")
      return("Hiba!")



if __name__ == "__main__":
    import sys
    import time
    import requests


    def on_click(self):
     if (len(ui.lineEdit.text()) != 0 ):
       print(ui.lineEdit.text())
       if (check_internet(self) == 1):
           cond = getWeather(ui.lineEdit.text())
           if (cond != "Hiba!"):
             ui.labelCity.setText(ui.lineEdit.text())
             refresh_Ui('0', cond)
           else:
               ui.labelCity.setText(cond)
               refresh_Ui('1','')
       else:
           ui.labelCity.setText("Hiba! Kérem  ellenőrizze az \n internetkapcsolatot!")
           refresh_Ui('2','')


    def refresh_Ui(condN, cond):
     if condN == "2": print('Internet hiba!'), clear_Ui()
     if condN == "1": print('Település név hiba!'), clear_Ui()
     if condN == "0": print('Minden jó'),ui.labelPicto.setStyleSheet("border-image:url(./images/"+cond[2]+".png)"),ui.labelCity.setStyleSheet("color:black;"), ui.labelTemp.setText(cond[0]), ui.labelDescript.setText(cond[1]), ui.labelTempMin.setText(cond[3]), ui.labelTempMax.setText(cond[4]), ui.labelTempFeel.setText(cond[5]),ui.labelHumidityPer.setText(cond[6]) , ui.labelWindSpeed.setText(cond[7]), ui.lineEdit.clear()

    def clear_Ui():
        ui.labelTempFeel.clear()
        ui.labelHumidityPer.clear()
        ui.labelTempMax.clear()
        ui.labelTempMin.clear()
        ui.labelTemp.clear()
        ui.labelWindSpeed.clear()
        ui.labelPicto.setStyleSheet("")
        ui.labelDescript.clear()
        ui.labelCity.setStyleSheet("color:red;")


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

