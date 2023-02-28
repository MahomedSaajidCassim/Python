# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assign2.ui'
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
        Dialog.resize(767, 645)
        self.lcdSa = QtGui.QLCDNumber(Dialog)
        self.lcdSa.setGeometry(QtCore.QRect(90, 170, 231, 81))
        self.lcdSa.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.lcdSa.setObjectName(_fromUtf8("lcdSa"))
        self.lcdJap = QtGui.QLCDNumber(Dialog)
        self.lcdJap.setGeometry(QtCore.QRect(440, 170, 241, 81))
        self.lcdJap.setObjectName(_fromUtf8("lcdJap"))
        self.projname = QtGui.QTextEdit(Dialog)
        self.projname.setGeometry(QtCore.QRect(70, 20, 611, 71))
        self.projname.setFocusPolicy(QtCore.Qt.NoFocus)
        self.projname.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.projname.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.projname.setObjectName(_fromUtf8("projname"))
        self.tsa = QtGui.QTextEdit(Dialog)
        self.tsa.setGeometry(QtCore.QRect(130, 120, 151, 31))
        self.tsa.setObjectName(_fromUtf8("tsa"))
        self.tj = QtGui.QTextEdit(Dialog)
        self.tj.setGeometry(QtCore.QRect(470, 120, 151, 31))
        self.tj.setObjectName(_fromUtf8("tj"))
        self.textEdit_6 = QtGui.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(120, 300, 151, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(470, 300, 151, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.flagSa = QtGui.QGraphicsView(Dialog)
        self.flagSa.setGeometry(QtCore.QRect(60, 360, 321, 211))
        self.flagSa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.flagSa.setObjectName(_fromUtf8("flagSa"))
        self.flagJap = QtGui.QGraphicsView(Dialog)
        self.flagJap.setGeometry(QtCore.QRect(430, 360, 301, 211))
        self.flagJap.setObjectName(_fromUtf8("flagJap"))
        self.projname.raise_()
        self.lcdSa.raise_()
        self.lcdJap.raise_()
        self.tsa.raise_()
        self.tj.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.flagSa.raise_()
        self.flagJap.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.projname.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Time In South Africa &amp; Time In Japan With Their Flags</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline;\"><br /></p></body></html>", None))
        self.tsa.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Time In South Africa</span></p></body></html>", None))
        self.tj.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Time In Japan</span></p></body></html>", None))
        self.textEdit_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Flag Of Country</span></p></body></html>", None))
        self.textEdit_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Flag Of Country</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

