import sys
from listoper import *
from PyQt4.QtGui import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem('Pizza')
        self.ui.listWidget.addItem('Hot Dog')
        self.ui.listWidget.addItem('French Fries')
        self.ui.listWidget.addItem('Chicken Burgar')
        QtCore.QObject.connect(self.ui.AddButton, QtCore.SIGNAL('clicked()'),
        self.addlist)
        QtCore.QObject.connect(self.ui.EditButton, QtCore.SIGNAL('clicked()'),
        self.editlist)
        QtCore.QObject.connect(self.ui.DeleteButton, QtCore.SIGNAL('clicked()'),
        self.delitem)
        QtCore.QObject.connect(self.ui.DeleteAllButton, QtCore.SIGNAL('clicked()'),
        self.delallitems)
        
    def addlist(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()
    def editlist(self):
        row=self.ui.listWidget.currentRow()
        newtext, ok=QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and (len(newtext) !=0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row,QListWidgetItem(newtext))
    def delitem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    def delallitems(self):
        self.ui.listWidget.clear()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

