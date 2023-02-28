import sys
from assign2 import *

class MyForm(QtGui.QDialog):
    def __init__(self, pixmap, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()

        timer2 = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd2)
        timer.start(1000)
        self.showlcd2()

        self.scene=QtGui.QGraphicsScene(self)
        self.scene.addPixmap(pixmap1)
        self.ui.flagSa.setScene(self.scene)
        
        self.scene2=QtGui.QGraphicsScene(self)
        self.scene2.addPixmap(pixmap2)
        self.ui.flagJap.setScene(self.scene2)

    def showlcd(self):
        time= QtCore.QTime.currentTime()
        text=time.toString('hh:mm')
        self.ui.lcdSa.display(text)

    def showlcd2(self):
        time2 = QtCore.QTime.currentTime()
        time2 = time2.addSecs(7 * 60 * 60)
        text2 =time2.toString('hh:mm')
        self.ui.lcdJap.display(text2)


if __name__ =="__main__":
    app =QtGui.QApplication(sys.argv)
    pixmap1=QtGui.QPixmap()
    pixmap1.load("saflag.png")
    pixmap2=QtGui.QPixmap()
    pixmap2.load("japflag.png")
    myapp=MyForm(pixmap1)
    myapp.show()
    sys.exit(app.exec())
