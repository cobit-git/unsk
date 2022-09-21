# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# creating a clock class
class Clock(QWidget):

    # constructor
    def __init__(self):
        super().__init__()

        self.color = True

        # creating timer
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        # setting window title
        self.setWindowTitle('U&SK Sound Detector')
        #self.setGeometry(200, 200, 300, 300)

        # create the label that holds the digital clock
        self.d_clock_width = 200
        self.d_clock_height = 50
        self.d_clock_label = QLabel(self)
        self.d_clock_label.setStyleSheet("border: 1px solid black;background-color: yellow;")
        self.d_clock_label.move(0, 0)
        self.d_clock_label.resize(self.d_clock_width, self.d_clock_height)

        # create the label that holds the distance
        self.distance_width = 200
        self.distance_height = 50
        self.distance_label = QLabel(self)
        self.distance_label.setStyleSheet("border: 2px solid black;")
        self.distance_label.move(200, 0)
        self.distance_label.resize(self.distance_width, self.distance_height)

        # create the label that holds the horn
        self.horn_width = 100
        self.horn_height = 100
        self.horn_label = QLabel(self)
        self.horn_pix = QPixmap('crash.png')
        self.horn_pix_s = self.horn_pix.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.horn_label.setPixmap(self.horn_pix_s)
        self.horn_label.setStyleSheet("border: 1px solid black;")
        self.horn_label.move(0, 50)
        self.horn_label.resize(self.horn_width, self.horn_height)

        # create the label that holds the ciren
        self.ciren_width = 100
        self.ciren_height = 100    # 
        self.ciren_label = QLabel(self)
        self.ciren_label.setStyleSheet("border: 2px solid black;")
        self.ciren_label.move(100, 50)
        self.ciren_label.resize(self.ciren_width, self.ciren_height)

        # create the label that holds the bike
        self.bike_width = 100
        self.bike_height = 100
        self.bike_label = QLabel(self)
        self.bike_label.setStyleSheet("border: 1px solid black;")
        self.bike_label.move(200, 50)
        self.bike_label.resize(self.bike_width, self.bike_height)

        # create the label that holds the crash
        self.crash_width = 100
        self.crash_height = 100
        self.crash_label = QLabel(self)
        self.crash_label.setStyleSheet("border: 2px solid black;")
        self.crash_label.move(300, 50)
        self.crash_label.resize(self.crash_width, self.ciren_height)

        # create the label that holds the clock
        self.clock_width = 400
        self.clock_height = 400
        self.clock_label = QLabel(self)
        self.clock_label.setStyleSheet("border: 3px solid black;")
        self.clock_label.move(0, 50)
        self.clock_label.resize(self.clock_width, self.clock_height)

        v_box = QVBoxLayout()
        h_1_box = QHBoxLayout()
        h_1_box.addWidget(self.d_clock_label)
        h_1_box.addWidget(self.distance_label)
        h_2_box = QHBoxLayout()
        h_2_box.addWidget(self.horn_label)
        h_2_box.addWidget(self.ciren_label)
        h_2_box.addWidget(self.bike_label)
        h_2_box.addWidget(self.crash_label)
        v_box.addLayout(h_2_box)
        v_box.addWidget(self.clock_label)

     # method for paint event
    def paintEvent(self, event):
        pass
    #def change_label_color(self):
    #    if self.color != True:
    #        self.d_clock_label.setStyleSheet("border: 1px solid black;background-color: yellow;")
    #    else:
    #        self.d_clock_label.setStyleSheet("border: 1px solid black;background-color: blue;")

  

# Driver code
if __name__ == '__main__':
	
    app = QApplication(sys.argv)
        
    # creating a clock object
    win = Clock()
        
    # show
    win.show()
	
exit(app.exec_())
