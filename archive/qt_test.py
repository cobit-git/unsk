from PyQt5.QtWidgets import *
import sys
import tensorflow
import librosa

class Dialog(QDialog):
   def slot_method(self):
		   print("Calling the slot")
   def __init__(self):
		   super(Dialog,self).__init__()
		   button=QPushButton("Click me")
		   button.clicked.connect(self.slot_method)
		   mainLayout=QVBoxLayout()
		   mainLayout.addWidget(button)
		   self.setLayout(mainLayout)
		   self.setWindowTitle("Hello, world!")
if __name__=='__main__':
   print(tensorflow.__version__)
   print(librosa.__version__)
   app=QApplication(sys.argv)
   dialog=Dialog()
dialog.exec_()
