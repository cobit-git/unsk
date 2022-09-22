# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# creating a clock class
class Unsk(QWidget):

    # constructor
    def __init__(self):
        super().__init__()

        # setting window title
        self.setWindowTitle('U&SK Sound Detector')
        #self.setGeometry(200, 200, 400, 800)

        # create the label that holds the digital clock
        font = QFont('Arial', 30, QFont.Bold)
        #self.d_clock_width = 200
        #self.d_clock_height = 50
        
        self.d_clock_label = QLabel(self)
        self.d_clock_label.setMinimumHeight(50)
        self.d_clock_label.setMinimumWidth(200)
        self.d_clock_label.setFont(font)
        self.d_clock_label.setStyleSheet("border: 1px solid black;background-color: yellow;")
        #self.d_clock_label.move(0, 0)
        #self.d_clock_label.resize(self.d_clock_width, self.d_clock_height)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # create the label that holds the distance
        #self.distance_width = 200
        #self.distance_height = 50
        self.distance_label = QLabel(self)
        self.distance_label.setMinimumHeight(50)
        self.distance_label.setMinimumWidth(200)
        self.distance_label.setStyleSheet("border: 1px solid black;")
        #self.distance_label.move(200, 0)
        #self.distance_label.resize(self.distance_width, self.distance_height)

        # create the label that holds the horn
        #self.horn_width = 100
        #self.horn_height = 100
        self.horn_label = QLabel(self)
        self.horn_label.setMinimumHeight(100)
        self.horn_label.setMinimumWidth(100)
        self.horn_pix = QPixmap('horn.png')
        self.horn_pix_s = self.horn_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.horn_label.setPixmap(self.horn_pix_s)
        self.horn_label.setAlignment(Qt.AlignCenter)
        self.horn_label.setStyleSheet("border: 1px solid black;")
        #self.horn_label.move(0, 50)
        #self.horn_label.resize(self.horn_width, self.horn_height)

        # create the label that holds the ciren
        #self.ciren_width = 100
        #self.ciren_height = 100    # 
        self.ciren_label = QLabel(self)
        self.ciren_label.setMinimumHeight(100)
        self.ciren_label.setMinimumWidth(100)
        self.ciren_pix = QPixmap('ciren.png')
        self.ciren_pix_s = self.ciren_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ciren_label.setPixmap(self.ciren_pix_s)
        self.ciren_label.setAlignment(Qt.AlignCenter)
        self.ciren_label.setStyleSheet("border: 1px solid black;")
        #self.ciren_label.move(100, 50)
        #self.ciren_label.resize(self.ciren_width, self.ciren_height)

        # create the label that holds the bike
        #self.bike_width = 100
        #self.bike_height = 100
        self.bike_label = QLabel(self)
        self.bike_label.setMinimumHeight(100)
        self.bike_label.setMinimumWidth(100)
        self.bike_pix = QPixmap('bike.png')
        self.bike_pix_s = self.bike_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.bike_label.setPixmap(self.bike_pix_s)
        self.bike_label.setAlignment(Qt.AlignCenter)
        self.bike_label.setStyleSheet("border: 1px solid black;")
        #self.bike_label.move(200, 50)
        #self.bike_label.resize(self.bike_width, self.bike_height)

        # create the label that holds the crash
        #self.crash_width = 100
        #self.crash_height = 100
        self.crash_label = QLabel(self)
        self.crash_label.setMinimumHeight(100)
        self.crash_label.setMinimumWidth(100)
        self.crash_pix = QPixmap('crash.png')
        self.crash_pix_s = self.crash_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.crash_label.setPixmap(self.crash_pix_s)
        self.crash_label.setAlignment(Qt.AlignCenter)
        self.crash_label.setStyleSheet("border: 1px solid black;")
        #self.crash_label.move(300, 50)
        #self.crash_label.resize(self.crash_width, self.ciren_height)

        # create the label that holds the clock
        
        #self.clock_width = 400
        #self.clock_height = 400
        self.clock_label = Clock()
        self.clock_label.setMinimumHeight(400)
        self.clock_label.setMinimumWidth(400)
        self.clock_label.setStyleSheet("border: 1px solid black;")
        #self.clock_label.move(0, 150)
        #self.clock_label.resize(self.clock_width, self.clock_height)
    
        # create the label that holds the clock
        
        #self.wave_width = 400
        #self.wave_height = 100
        self.wave_label = Wave()
        self.wave_label.setMinimumHeight(100)
        self.wave_label.setMinimumWidth(400)
        self.wave_label.setStyleSheet("border: 1px solid black;")
        #self.wave_label.move(0, 150)
        #self.wave_label.resize(self.wave_width, self.wave_height)
    

        v_box = QVBoxLayout()
        h_1_box = QHBoxLayout()
        h_1_box.addWidget(self.d_clock_label)
        h_1_box.addWidget(self.distance_label)
        h_2_box = QHBoxLayout()
        h_2_box.addWidget(self.horn_label)
        h_2_box.addWidget(self.ciren_label)
        h_2_box.addWidget(self.bike_label)
        h_2_box.addWidget(self.crash_label)
        v_box.addLayout(h_1_box)
        v_box.addLayout(h_2_box)
        v_box.addWidget(self.clock_label)
        v_box.addWidget(self.wave_label)
        self.setLayout(v_box)
    
    # method called by timer
    def showTime(self):
  
        # getting current time
        current_time = QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.d_clock_label.setText(label_time)

class Clock(QLabel):
    # constructor
    def __init__(self):
        super().__init__()
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        # creating hour hand
        self.hPointer = QtGui.QPolygon([QPoint(6, 7),QPoint(-6, 7),QPoint(0, -50)])
        # creating minute hand
        self.mPointer = QPolygon([QPoint(6, 7),QPoint(-6, 7),QPoint(0, -70)])
        # creating second hand
        self.sPointer = QPolygon([QPoint(1, 1),QPoint(-1, 1),QPoint(0, -90)])
        # color for minute and hour hand
        self.bColor = Qt.green
        # color for second hand
        self.sColor = Qt.red

    def paintEvent(self, event):
        # so that clock remain square
        rec = min(self.width(), self.height())
        # getting current time
        tik = QTime.currentTime()
        # creating a painter object
        painter = QPainter(self)
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, rotation, pointer):
            # setting brush
            painter.setBrush(QBrush(color))
            # saving painter
            painter.save()
            # rotating painter
            painter.rotate(rotation)
            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)
            # restore the painter
            painter.restore()
        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)
        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)
        # scale the painter
        painter.scale(rec / 200, rec / 200)
        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)
        # draw each hand
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
        # drawing background
        painter.setPen(QPen(self.bColor))
        # for loop
        for i in range(0, 60):
            # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)
            # rotating the painter
            painter.rotate(6)
        # ending the painter
        painter.end()

class Wave(QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

# Driver code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Unsk()
    win.show()
exit(app.exec_())
