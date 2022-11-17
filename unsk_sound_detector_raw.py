#  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
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import numpy as np
import math

from time_setting import TimeSetting, TimeData
from unsk_sound_thread import SoundDetector, UnskData
from threading import Timer

# creating a clock class
class Unsk(QWidget):

    # constructor
    def __init__(self):
        super().__init__()

        # setting window title
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle('no title')
        #self.setGeometry(200, 200, 400, 800)

        self.sys_clock = True
        self.ui_run = False

        self.hour = 0
        self.min = 0
        self.second = 0


        # create the label that holds the digital clock
        font = QFont('Arial', 30)
        #self.d_clock_width = 200
        #self.d_clock_height = 50
        
        self.d_clock_label = QLabel(self)
        self.d_clock_label.setMinimumHeight(50)
        self.d_clock_label.setMinimumWidth(200)
        self.d_clock_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_clock_label.setFont(font)
        self.d_clock_label.setStyleSheet("background: lightgray;")
        #self.d_clock_label.move(0, 0)
        #self.d_clock_label.resize(self.d_clock_width, self.d_clock_height)
       
        # create the label that holds the distance
        #self.distance_width = 200
        #self.distance_height = 50
        self.distance_label = QLabel(self)
        self.distance_label.setMinimumHeight(50)
        self.distance_label.setMinimumWidth(200)
        self.distance_label.setFont(font)
        self.distance_label.setAlignment(QtCore.Qt.AlignRight)
        self.distance_label.setText(str(0)+' m')
        #self.distance_label.setStyleSheet("border: 1px solid black;background: light gray;")
        self.distance_label.setStyleSheet("background: lightgray;")
        
        #self.distance_label.move(200, 0)
        #self.distance_label.resize(self.distance_width, self.distance_height)

        # create the label that holds the horn
        #self.horn_width = 100
        #self.horn_height = 100
        self.horn_label = QLabel(self)
        self.horn_label.setMinimumHeight(100)
        self.horn_label.setMinimumWidth(100)
        self.horn_pix = QPixmap('./image/claxon1.png')
        self.horn_pix_s = self.horn_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.horn_pix_2 = QPixmap('./image/claxon3.png')
        self.horn_pix_2_s = self.horn_pix_2.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.horn_label.setPixmap(self.horn_pix_s)
        self.horn_label.setAlignment(Qt.AlignCenter)
        self.horn_label.setStyleSheet("background: white;")
        #self.horn_label.move(0, 50)
        #self.horn_label.resize(self.horn_width, self.horn_height)

        # create the label that holds the ciren
        #self.ciren_width = 100
        #self.ciren_height = 100    # 
        self.ciren_label = QLabel(self)
        self.ciren_label.setMinimumHeight(100)
        self.ciren_label.setMinimumWidth(100)
        self.ciren_pix = QPixmap('./image/siren1.png')
        self.ciren_pix_s = self.ciren_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ciren_pix_2 = QPixmap('./image/siren3.png')
        self.ciren_pix_2_s = self.ciren_pix_2.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ciren_label.setPixmap(self.ciren_pix_s)
        self.ciren_label.setAlignment(Qt.AlignCenter)
        self.ciren_label.setStyleSheet("background: white;")
        #self.ciren_label.move(100, 50)
        #self.ciren_label.resize(self.ciren_width, self.ciren_height)

        # create the label that holds the bike
        #self.bike_width = 100
        #self.bike_height = 100
        self.bike_label = QLabel(self)
        self.bike_label.setMinimumHeight(100)
        self.bike_label.setMinimumWidth(100)
        self.bike_pix = QPixmap('./image/motorcycle1.png')
        self.bike_pix_s = self.bike_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.bike_pix_2 = QPixmap('./image/motorcycle3.png')
        self.bike_pix_2_s = self.bike_pix_2.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.bike_label.setPixmap(self.bike_pix_s)
        self.bike_label.setAlignment(Qt.AlignCenter)
        self.bike_label.setStyleSheet("background: white;")
        #self.bike_label.move(200, 50)
        #self.bike_label.resize(self.bike_width, self.bike_height)

        # create the label that holds the crash
        #self.crash_width = 100
        #self.crash_height = 100
        self.crash_label = QLabel(self)
        self.crash_label.setMinimumHeight(100)
        self.crash_label.setMinimumWidth(100)
        self.crash_pix = QPixmap('./image/carcrash1.png')
        self.crash_pix_s = self.crash_pix.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.crash_pix_2 = QPixmap('./image/carcrash3.png')
        self.crash_pix_2_s = self.crash_pix_2.scaled(80, 80, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.crash_label.setPixmap(self.crash_pix_s)
        self.crash_label.setAlignment(Qt.AlignCenter)
        self.crash_label.setStyleSheet("background: white;")
        #self.crash_label.move(300, 50)
        #self.crash_label.resize(self.crash_width, self.ciren_height)

        # create the label that holds the clock
        
        #self.clock_width = 400
        #self.clock_height = 400
        self.clock_label = Clock()
        self.clock_label.setMinimumHeight(400)
        self.clock_label.setMinimumWidth(400)
        self.clock_label.setStyleSheet("background: lightgray;")
        #self.clock_label.move(0, 150)
        #self.clock_label.resize(self.clock_width, self.clock_height)
    
        # create the label that holds the clock
        
        #self.wave_width = 400
        #self.wave_height = 100
        self.wave_label = Wave()
        self.wave_label.setMinimumHeight(100)
        self.wave_label.setMinimumWidth(400)
        self.wave_label.setStyleSheet("background: lightgray;")
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

        self.thread = SoundDetector()
        self.thread.sound_signal.connect(self.update_signal)
        self.thread.sound_signal.connect(self.wave_label.update_signal_wave)
        
        self.timeSetting()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.thread.start()

    def timeSetting(self):
        timePopup = TimeSetting(self)
        timePopup.time_signal.connect(self.update_time)
        timePopup.setGeometry(100, 200, 100, 100)
        timePopup.show()

    
    # method called by timer
    def showTime(self):
        if self.ui_run == True:
            # getting current time
            if self.sys_clock == True:
                current_time = QTime.currentTime() 
                # converting QTime object to string
                label_time = current_time.toString('hh:mm:ss')
                # showing it to the label
                self.d_clock_label.setText(label_time)
            else:
                current_time = QTime.currentTime() 
                self.second += 1
                if self.second > 59:
                    self.min += 1
                    self.second = 0
                if self.min > 59:
                    self.hour += 1
                    self.min = 0
                if self.hour > 23:
                    self.hour = 0
                
                self.d_clock_label.setText(str(self.hour).zfill(2)+':'+str(self.min).zfill(2)+':'+str(self.second).zfill(2))
           
        else:
            self.d_clock_label.setText('00:00:00')

    @pyqtSlot(UnskData)
    def update_signal(self, signal_packet):
        if self.ui_run == True:
            if signal_packet.code == 0:
                self.distance_label.setText(str(signal_packet.distance)+" m")
                self.clock_label.distance = signal_packet.distance
                self.clock_label.isClock = False
                self.horn_label.setPixmap(self.horn_pix_2_s)
                #self.horn_label.setStyleSheet("Background: yellow;")
                #self.clock_label.setStyleSheet("Background: white;")
                self.run_once(self.reset_bg, signal_packet.code)
            elif signal_packet.code == 1:
                self.distance_label.setText(str(signal_packet.distance)+" m")
                self.clock_label.distance = signal_packet.distance
                self.clock_label.isClock = False
                self.ciren_label.setPixmap(self.ciren_pix_2_s)
                #self.ciren_label.setStyleSheet("Background: yellow;")
                #self.clock_label.setStyleSheet("Background: white;")
                self.run_once(self.reset_bg, signal_packet.code)
            elif signal_packet.code == 2:
                self.distance_label.setText(str(signal_packet.distance)+" m")
                self.clock_label.distance = signal_packet.distance
                self.clock_label.isClock = False
        
                self.bike_label.setPixmap(self.bike_pix_2_s)
                #self.bike_label.setStyleSheet("Background: yellow;")
                #self.clock_label.setStyleSheet("Background: white;")
                self.run_once(self.reset_bg, signal_packet.code)
            elif signal_packet.code == 3:
                self.distance_label.setText(str(signal_packet.distance)+" m")
                self.clock_label.distance = signal_packet.distance
                self.clock_label.isClock = False
                self.crash_label.setPixmap(self.crash_pix_2_s)
                #self.crash_label.setStyleSheet("Background: yellow;")
                #self.clock_label.setStyleSheet("Background: white;")
                self.run_once(self.reset_bg, signal_packet.code)

  
    def reset_bg(self, code):
        self.clock_label.setStyleSheet("Background: lightgray;")
        if code == 0:
            self.horn_label.setPixmap(self.horn_pix_s)
            self.horn_label.setStyleSheet("Background: white;")
        elif code == 1:
            self.ciren_label.setPixmap(self.ciren_pix_s)
            self.ciren_label.setStyleSheet("Background: white;")
        elif code == 2:
            self.bike_label.setPixmap(self.bike_pix_s)
            self.bike_label.setStyleSheet("Background: white;")
        elif code == 3:
            self.crash_label.setPixmap(self.crash_pix_s)
            self.crash_label.setStyleSheet("Background: white;")
        self.clock_label.isClock = True

    def run_once(self, func, code):  
        t=Timer(3, func, [code])  
        t.start()#Here run is called  

    @pyqtSlot(TimeData)
    def update_time(self, TimeData):
        print(TimeData.hour, TimeData.min, TimeData.second, TimeData.sys_clock)
        self.ui_run = True
        self.sys_clock = TimeData.sys_clock
        self.hour = TimeData.hour
        self.min = TimeData.min
        self.second = TimeData.second
        self.clock_label.set_work(True)
        self.wave_label.set_work(True)
        self.clock_label.set_sys_clock(TimeData.sys_clock)
        self.clock_label.time_setting(TimeData.hour, TimeData.min, TimeData.second)

class Clock(QLabel):
    # constructor
    def __init__(self):
        super().__init__()

        self.ui_run = False
        self.sys_clock = False

        self.hour = 0
        self.min = 0
        self.second = 0

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        timer2 = QTimer(self)
        timer2.timeout.connect(self.timer2_clock)
        timer2.start(1000)

        self.direction_img = QPixmap('./image/bar.png')

        # creating hour hand
        self.hPointer = QtGui.QPolygon([QPoint(3, 7),QPoint(-3, 7),QPoint(-3, -50), QPoint(3, -50)])
        # creating minute hand
        self.mPointer = QPolygon([QPoint(2, 7),QPoint(-2, 7),QPoint(-2, -70), QPoint(2, -70)])
        # creating second hand
        self.sPointer = QPolygon([QPoint(1, 1),QPoint(-1, 1),QPoint(-1, -90), QPoint(1, -90)])
        # color for minute and hour hand
        self.dPointer = QPolygon([QPoint(2, 9),QPoint(-2, 9),QPoint(-2, -80), QPoint(2, -80)])
        # color for minute and hour hand
        self.hColor = Qt.blue
        self.mColor = Qt.blue
        self.sColor = Qt.red
        self.bColor = Qt.black
        self.dColor = Qt.red

        self.distance  = 0

        self.isClock = True

    def timer2_clock(self):
        self.second += 1
        if self.second > 59:
            self.min += 1
            self.second = 0
        if self.min > 59:
            self.hour += 1
            self.min = 0
        if self.hour > 23:
            self.hour = 0


    def set_sys_clock(self, flag):
        self.sys_clock = flag 

    def time_setting(self, hour, min, sec):
        self.hour = hour
        self.min = min 
        self.second = sec 


    def set_work(self, flag):
        self.ui_run = flag

    def paintEvent(self, event):
        # so that clock remain square
        rec = min(self.width(), self.height())
        #if self.isClock: 
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
        painter.setPen(QPen(QBrush(Qt.transparent), 1))
        # draw each hand
        painter.save()
        if self.isClock == True:
            if self.ui_run == True:
                if self.sys_clock == True:
                    drawPointer(self.hColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
                    drawPointer(self.mColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
                    drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
                    #print(tik.hour(), tik.minute(), tik.second())
                else:
                    drawPointer(self.hColor, (30 * (self.hour + self.min / 60)), self.hPointer)
                    drawPointer(self.mColor, (6 * (self.min + self.second / 60)), self.mPointer)
                    drawPointer(self.sColor, (6 * self.second), self.sPointer)
                    
            else:
                drawPointer(self.hColor, 0, self.hPointer)
                drawPointer(self.mColor, 0, self.mPointer)
                drawPointer(self.sColor, 0, self.sPointer)
        else:
            painter.rotate(self.distance*2)
            painter.drawPixmap(self.rect(),self.direction_img)
            drawPointer(self.dColor, self.distance * 2, self.dPointer)
        # drawing background
        painter.restore()
        painter.setPen(QPen(self.bColor))
        # for loop
        if self.isClock == True:
            
            for i in range(0, 60):
                # drawing background lines
                if (i % 5) == 0:
                    painter.setPen(QPen(QBrush(Qt.black), 3))
                    painter.drawLine(87, 0, 97, 0)
                    painter.setPen(QPen(QBrush(Qt.transparent), 1))
                else:
                    painter.setPen(QPen(QBrush(Qt.black), 1))
                    painter.drawLine(92, 0, 97, 0)
                    painter.setPen(QPen(QBrush(Qt.transparent), 1))
                # rotating the painter
                painter.rotate(6)
                painter.setBrush(QBrush(self.bColor))
                painter.drawEllipse(-5, -5, 12, 12)
        else:
            for i in range(0, 60):
                # drawing background lines
                if (i % 5) == 0:
                    painter.setPen(QPen(QBrush(Qt.black), 3))
                    painter.drawLine(87, 0, 97, 0)
                    painter.setPen(QPen(QBrush(Qt.transparent), 1))
                else:
                    painter.setPen(QPen(QBrush(Qt.black), 1))
                    painter.drawLine(92, 0, 97, 0)
                    painter.setPen(QPen(QBrush(Qt.transparent), 1))
                # rotating the painter
                painter.rotate(6)
                painter.setBrush(QBrush(self.hColor))
                #painter.drawEllipse(-5, -5, 10, 10)
    
        # ending the painter
        painter.end()


    
class Wave(QLabel):
    def __init__(self):
        super().__init__()
        self.sound = np.ones(100)
        self.isUniqueSound = False
        self.ui_run = False
   
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.drawWave()
        self.painter.end()

    def drawWave(self):
        pen = QPen(Qt.black, 3)
        self.painter.setPen(pen)
        for i in range(1, 100):
            self.painter.drawLine(5*i, 100-5, 5*i, 100-self.sound[i])

    def set_work(self, flag):
        self.ui_run = flag

    @pyqtSlot(UnskData)  # receive unsk sound detector event 
    def update_signal_wave(self, signal_packet):
        if self.ui_run == True:
            # NOT detecting status 
            if signal_packet.code == 4 and self.isUniqueSound == False:
                self.sound = signal_packet.sound
                self.update()  # to call paintEvent()
            # detecting status 
            elif self.isUniqueSound == False:
                self.isUniqueSound = True
                self.sound = signal_packet.sound
                self.run_once(self.clear_unique)
                self.update() 
        
    def run_once(self, func):  
        t=Timer(3, func)  
        t.start()#Here run is called  

    def clear_unique(self):
        self.isUniqueSound = False
       
# Driver code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Unsk()
    win.show()
exit(app.exec_())
