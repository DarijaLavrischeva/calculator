import re
from decimal import *
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from thatiscalc import Ui_MainWindow

from PySide6.QtGui import QFontDatabase

regexstr = r'/^(\+|-)?(\d{1,3})((( ?(\d{3}))?)+)((\.|,)(\d{1,6}))?$/g'


class Calculator(QMainWindow):

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.eqButton.clicked.connect(self.calculate)
        self.ui.butBuhg.clicked.connect(self.buhgeq)
        self.ui.butMath.clicked.connect(self.matheq)
        self.ui.butUsec.clicked.connect(self.cutoff)

    def calculate(self):
        inperrflag = False
        strN_1 = self.ui.r_num1.text()
        strN_2 = self.ui.r_num2.text()
        strN_3 = self.ui.r_num3.text()
        strN_4 = self.ui.r_num4.text()
        alr = '0'
        zn1 = self.ui.znak1.currentText()
        zn2 = self.ui.znak2.currentText()
        zn3 = self.ui.znak3.currentText()

        middlesum = 0

        if re.fullmatch(r'^((\+)|-)?(\d{1,3})((( ?(\d{3}))?)+)(((\.)|,)(\d{1,10}))?$', strN_1):
            strN_1 = strN_1.replace(',', '.')
            strN_1 = strN_1.replace(' ', '')
            strN_1 = Decimal(strN_1)

        elif strN_1 == '':
            strN_1 = Decimal(0)
            zn1 = '+'

        else:
            alr = alr+'1'
            inperrflag = True

        if re.fullmatch(r'^((\+)|-)?(\d{1,3})((( ?(\d{3}))?)+)(((\.)|,)(\d{1,10}))?$', strN_2):
            strN_2 = strN_2.replace(',', '.')
            strN_2 = strN_2.replace(' ', '')
            strN_2 = Decimal(strN_2)

        elif strN_2 == '':
            strN_2 = Decimal(0)
            zn2 = '+'

        else:
            alr = alr+'2'
            inperrflag = True

        if re.fullmatch(r'^((\+)|-)?(\d{1,3})((( ?(\d{3}))?)+)(((\.)|,)(\d{1,10}))?$', strN_3):
            strN_3 = strN_3.replace(',', '.')
            strN_3 = strN_3.replace(' ', '')
            strN_3 = Decimal(strN_3)

        elif strN_3 == '':
            strN_3 = Decimal(0)
            zn2 = '+'

        else:
            alr = alr+'3'
            inperrflag = True

        if re.fullmatch(r'^((\+)|-)?(\d{1,3})((( ?(\d{3}))?)+)(((\.)|,)(\d{1,10}))?$', strN_4):
            strN_4 = strN_4.replace(',', '.')
            strN_4 = strN_4.replace(' ', '')
            strN_4 = Decimal(strN_4)

        elif strN_4 == '':
            strN_4 = Decimal(0)
            zn3 = '+'

        else:
            alr = alr+'4'
            inperrflag = True

        #if inperrflag:
            #self.ui.rezLabel1.setText(alr)
        #else:
         #   self.ui.rezLabel1.setText('congrats')
        wrongs = False
        outofb = False
        middlesum = Decimal(0)
        resN = Decimal(0)

        if inperrflag:
            warstr = str(alr) + 'wrong input'
            self.ui.rezLabel1.setText(warstr)
        else:

            if zn2 == '+':
                middlesum = Decimal(strN_2 + strN_3)
                # self.ui.rezLabel1.setText(str(middlesum))
            elif zn2 == '*':
                middlesum = Decimal(strN_2 * strN_3)
                # self.ui.rezLabel1.setText(str(middlesum))
            elif zn2 == '/':
                if (strN_3 == 0):
                    # self.ui.rezLabel1.setText('middle sum crashed: dividing by zero')
                    wrongs = True
                else:
                    middlesum = Decimal(strN_2 / strN_3)
                    # self.ui.rezLabel1.setText(str(middlesum))
            elif zn2 == '-':
                middlesum = Decimal(strN_2 - strN_3)
                # self.ui.rezLabel1.setText(str(middlesum))
            # else:
            # self.ui.rezLabel1.setText('middle sum crashed: god hates us for smth')
            if middlesum>1000000000000:
                outofb = True

            resN = Decimal(middlesum)

            if zn1 == '*':
                resN = Decimal(strN_1 * resN)
                # self.ui.rezLabel1.setText(str(resN))
            if zn1 == '/':
                if middlesum == 0:
                    # self.ui.rezLabel1.setText('dividing by zero(1)')
                    wrongs = True
                else:
                    resN = Decimal(strN_1 / resN)

            if middlesum>1000000000000:
                outofb = True

            if zn3 == '*':
                resN = Decimal(strN_4 * resN)

            if zn3 == '/':
                if strN_4 == 0:
                    wrongs = True
                else:
                    resN = Decimal(resN / strN_4)

            if middlesum>1000000000000:
                outofb = True

            if zn1 == '+':
                resN = Decimal(resN + strN_1)

            if zn1 == '-':
                resN = Decimal(strN_1 - resN)

            if zn3 == '+':
                resN = Decimal(resN + strN_4)

            if zn3 == '-':
                resN = Decimal(resN - strN_4)

            if middlesum>1000000000000:
                outofb = True

        if wrongs:
            self.ui.rezLabel1.setText('dividing by zero')
        elif outofb:
            self.ui.rezLabel1.setText('inner calculation is out of bounds of 1 000 000 000 000')
        else:
            resstr = format(resN.normalize(),'^10,.10f').replace(',',' ').rstrip('0').rstrip('.')
            # if resstr.partition('.')[2] == '':
            #     resstr = resstr + '0'

            self.ui.rezLabel1.setText(resstr)


    def buhgeq(self):

        befeq = self.ui.rezLabel1.text()

        if (befeq[0].isdigit() or befeq[0]=='-'):

            lpart = befeq.partition('.')[0]
            lpart = Decimal(lpart.replace(' ', ''))
            rpart = befeq.partition('.')[2]
            if rpart == '':
                rpartpart = 0
            else:
                rpartpart = int(rpart[0])
                if (rpartpart == 5 and int(rpart)>10):
                    if(int(rpart[1]) >= 5):
                        rpartpart = 6


            rez = 0

            if rpartpart<5:
                rez = lpart
            elif rpartpart>5:
                rez = lpart+1
            else:
                if lpart%2==1:
                    rez = lpart+1
                else:

                    rez = lpart

            self.ui.rezLabel2.setText(str(rez))

        else:
            self.ui.rezLabel2.setText('you already have error')




    def matheq(self):
        befeq = self.ui.rezLabel1.text()

        if (befeq[0].isdigit() or befeq[0]=='-'):

            lpart = befeq.partition('.')[0]
            lpart = Decimal(lpart.replace(' ', ''))
            rpart = befeq.partition('.')[2]
            if rpart == '':
                rpartpart = 0
            else:
                rpartpart = int(rpart[0])

            rez = 0

            if rpartpart < 5:
                rez = lpart
            elif rpartpart >= 5:
                rez = lpart + 1

            self.ui.rezLabel2.setText(str(rez))

        else:
            self.ui.rezLabel2.setText('you already have error')


    def cutoff(self):
        befeq = self.ui.rezLabel1.text()

        if (befeq[0].isdigit() or befeq[0]=='-'):

            lpart = befeq.partition('.')[0]
            lpart = Decimal(lpart.replace(' ', ''))

            rez = lpart

            self.ui.rezLabel2.setText(str(rez))

        else:
            self.ui.rezLabel2.setText('you already have error')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())




    '''
    
    def calculate(self):
        inperrflag = False
        strN_1 = self.ui.r_num1.text()
        strN_2 = self.ui.r_num2.text()
        strN_3 = self.ui.r_num3.text()
        strN_4 = self.ui.r_num4.text()

        zn1 = self.ui.znak1.text()
        zn2 = self.ui.znak2.text()
        zn3 = self.ui.znak3.text()

        if re.fullmatch(regexstr, strN_1):
            strN_1 = strN_1.replace(',', '.')
            strN_1 = strN_1.replace(' ', '')
            strN_1 = Decimal(strN_1)
            inperrflag = False
        elif strN_1 == '':
            strN_1 = 0
            zn1 = '+'
            inperrflag = False
        else:
            inperrflag = True

        if re.fullmatch(regexstr, strN_2):
            strN_2 = strN_2.replace(',', '.')
            strN_2 = strN_2.replace(' ', '')
            strN_2 = Decimal(strN_2)
            inperrflag = False
        elif strN_2 == '':
            strN_2 = 0
            zn2 = '+'
            inperrflag = False
        else:
            inperrflag = True

        if re.fullmatch(regexstr, strN_3):
            strN_3 = strN_3.replace(',', '.')
            strN_3 = strN_3.replace(' ', '')
            strN_3 = Decimal(strN_3)
            inperrflag = False
        elif strN_3 == '':
            strN_3 = 0
            zn2 = '+'
            inperrflag = False
        else:
            inperrflag = True

        if re.fullmatch(regexstr, strN_4):
            strN_4 = strN_4.replace(',', '.')
            strN_4 = strN_4.replace(' ', '')
            strN_4 = Decimal(strN_4)
            inperrflag = False
        elif strN_4 == '':
            strN_4 = 0
            zn3 = '+'
            inperrflag = False
        else:
            inperrflag = True

        if inperrflag:
            self.ui.rezLabel1.setText('input error')
        else:
            self.ui.rezLabel1.setText('congrats')


    '''