import sys
from addtwonum2 import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.AddButton,   QtCore.SIGNAL('clicked()'), self.dispsum)
    def dispsum(self):
        if len(self.ui.lineFirstNumber.text())!=0:
            a=int(self.ui.lineFirstNumber.text())
        else:
            a=0
        if len(self.ui.lineSecondNumber.text())!=0:
            b=int(self.ui.lineSecondNumber.text())
        else:
            b=0
        sum=a+b
        self.ui.labelAddition.setText (str(sum))

if __name__ =="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
        
