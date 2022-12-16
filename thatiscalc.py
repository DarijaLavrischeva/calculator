# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thatiscalc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1091, 658)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.eqButton = QPushButton(self.centralwidget)
        self.eqButton.setObjectName(u"eqButton")
        self.eqButton.setGeometry(QRect(360, 160, 311, 81))
        self.r_num2 = QLineEdit(self.centralwidget)
        self.r_num2.setObjectName(u"r_num2")
        self.r_num2.setGeometry(QRect(290, 80, 201, 31))
        self.r_num3 = QLineEdit(self.centralwidget)
        self.r_num3.setObjectName(u"r_num3")
        self.r_num3.setGeometry(QRect(530, 80, 201, 31))
        self.znak2 = QComboBox(self.centralwidget)
        self.znak2.addItem("")
        self.znak2.addItem("")
        self.znak2.addItem("")
        self.znak2.addItem("")
        self.znak2.setObjectName(u"znak2")
        self.znak2.setGeometry(QRect(490, 80, 41, 31))
        self.rezLabel1 = QLineEdit(self.centralwidget)
        self.rezLabel1.setObjectName(u"rezLabel1")
        self.rezLabel1.setGeometry(QRect(200, 260, 281, 81))
        self.rezLabel1.setReadOnly(True)
        self.rezLabel2 = QLineEdit(self.centralwidget)
        self.rezLabel2.setObjectName(u"rezLabel2")
        self.rezLabel2.setGeometry(QRect(540, 260, 281, 81))
        self.rezLabel2.setReadOnly(True)
        self.butBuhg = QPushButton(self.centralwidget)
        self.butBuhg.setObjectName(u"butBuhg")
        self.butBuhg.setGeometry(QRect(200, 350, 281, 29))
        self.butUsec = QPushButton(self.centralwidget)
        self.butUsec.setObjectName(u"butUsec")
        self.butUsec.setGeometry(QRect(200, 390, 281, 29))
        self.butMath = QPushButton(self.centralwidget)
        self.butMath.setObjectName(u"butMath")
        self.butMath.setGeometry(QRect(200, 430, 281, 29))
        self.r_num4 = QLineEdit(self.centralwidget)
        self.r_num4.setObjectName(u"r_num4")
        self.r_num4.setGeometry(QRect(800, 80, 201, 31))
        self.r_num1 = QLineEdit(self.centralwidget)
        self.r_num1.setObjectName(u"r_num1")
        self.r_num1.setGeometry(QRect(20, 80, 201, 31))
        self.znak3 = QComboBox(self.centralwidget)
        self.znak3.addItem("")
        self.znak3.addItem("")
        self.znak3.addItem("")
        self.znak3.addItem("")
        self.znak3.setObjectName(u"znak3")
        self.znak3.setGeometry(QRect(760, 80, 41, 31))
        self.znak1 = QComboBox(self.centralwidget)
        self.znak1.addItem("")
        self.znak1.addItem("")
        self.znak1.addItem("")
        self.znak1.addItem("")
        self.znak1.setObjectName(u"znak1")
        self.znak1.setGeometry(QRect(220, 80, 41, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 80, 71, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(740, 80, 21, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hello attempt", None))
        self.eqButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.r_num3.setText("")
        self.znak2.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.znak2.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.znak2.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.znak2.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))

        self.butBuhg.setText(QCoreApplication.translate("MainWindow", u"accounting", None))
        self.butUsec.setText(QCoreApplication.translate("MainWindow", u"truncation", None))
        self.butMath.setText(QCoreApplication.translate("MainWindow", u"mathematical", None))
        self.znak3.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.znak3.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.znak3.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.znak3.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))

        self.znak1.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.znak1.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.znak1.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.znak1.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u")", None))
    # retranslateUi

