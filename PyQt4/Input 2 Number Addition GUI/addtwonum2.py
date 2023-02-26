# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtwonum2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(423, 272)
        self.labelFirstNumber = QtGui.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(30, 130, 121, 16))
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(160, 170, 111, 21))
        self.labelAddition.setText(_fromUtf8(""))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))
        self.lineFirstNumber = QtGui.QLineEdit(Dialog)
        self.lineFirstNumber.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.lineSecondNumber = QtGui.QLineEdit(Dialog)
        self.lineSecondNumber.setGeometry(QtCore.QRect(160, 130, 113, 20))
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.labelSecondNumber_2 = QtGui.QLabel(Dialog)
        self.labelSecondNumber_2.setGeometry(QtCore.QRect(30, 170, 121, 16))
        self.labelSecondNumber_2.setObjectName(_fromUtf8("labelSecondNumber_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number:", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number:", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))
        self.labelSecondNumber_2.setText(_translate("Dialog", "Total:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

