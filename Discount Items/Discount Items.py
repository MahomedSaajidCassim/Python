from __future__ import division
import sys
from discountitemsqt import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.calculate)

    def calculate(self):
        if len(self.ui.quantity.text())!=0:
            q=int(float(self.ui.lineEdit.text()))
        else:
            q=0
        if len(self.ui.rates.text())!=0:
            r=int(float(self.ui.lineEdit_2.text()))
        else:
            r=0
        if len(self.ui.discount.text())!=0:
            d=int(float(self.ui.lineEdit_3.text()))
        else:
            d=0
        totamt=q*r
        disc=totamt*d/100
        netamt=totamt-disc
        self.ui.results.setText("Total Amount: " +str(totamt) +", Discount: "+str(disc)+" , Net Amount: "+str(netamt))

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())
