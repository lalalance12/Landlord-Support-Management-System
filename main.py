import sys

import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'


from ui_interface import *

from functions import appFunctions

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
       
        
        
        
        self.show()
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    