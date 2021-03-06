import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.multiply)

    def multiply(self) :
        a = int(self.le1.text())
        b = int(self.le2.text())
        c = a * b
        self.le3.setText(str(c))
        
        # self.le3.setText(str(int(self.le1.text())* int(self.le2.text())))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()