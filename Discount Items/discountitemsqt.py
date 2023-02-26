# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buddytab.ui'
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
        Dialog.resize(400, 300)
        self.quantity = QtGui.QLabel(Dialog)
        self.quantity.setGeometry(QtCore.QRect(50, 40, 101, 16))
        self.quantity.setObjectName(_fromUtf8("quantity"))
        self.rates = QtGui.QLabel(Dialog)
        self.rates.setGeometry(QtCore.QRect(50, 80, 91, 16))
        self.rates.setObjectName(_fromUtf8("rates"))
        self.discount = QtGui.QLabel(Dialog)
        self.discount.setGeometry(QtCore.QRect(50, 120, 121, 16))
        self.discount.setObjectName(_fromUtf8("discount"))
        self.results = QtGui.QLabel(Dialog)
        self.results.setGeometry(QtCore.QRect(5, 210, 381, 71))
        self.results.setText(_fromUtf8(""))
        self.results.setObjectName(_fromUtf8("results"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 40, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 120, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 111, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.quantity.setBuddy(self.lineEdit)
        self.rates.setBuddy(self.lineEdit_2)
        self.discount.setBuddy(self.lineEdit_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.quantity.setText(_translate("Dialog", "&Number of Items", None))
        self.rates.setText(_translate("Dialog", "&Price per Item", None))
        self.discount.setText(_translate("Dialog", "&Discount Percentage", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Amount", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

