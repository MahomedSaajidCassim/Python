# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listoper.ui'
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
        Dialog.resize(744, 595)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.EditButton = QtGui.QPushButton(Dialog)
        self.EditButton.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.EditButton.setObjectName(_fromUtf8("EditButton"))
        self.DeleteButton = QtGui.QPushButton(Dialog)
        self.DeleteButton.setGeometry(QtCore.QRect(140, 240, 75, 23))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.DeleteAllButton = QtGui.QPushButton(Dialog)
        self.DeleteAllButton.setGeometry(QtCore.QRect(140, 310, 75, 23))
        self.DeleteAllButton.setObjectName(_fromUtf8("DeleteAllButton"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(300, 60, 291, 291))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Enter Text", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))
        self.EditButton.setText(_translate("Dialog", "Edit", None))
        self.DeleteButton.setText(_translate("Dialog", "Delete", None))
        self.DeleteAllButton.setText(_translate("Dialog", "Delete All", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

