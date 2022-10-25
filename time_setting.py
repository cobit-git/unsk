from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TimeData:
    def __init__(self):
        self.hour = 0
        self.min = 0
        self.second = 0
        self.sys_clock= True

class TimeSetting(QDialog): 
    
    time_packet = TimeData()
    time_signal = pyqtSignal(TimeData)
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.hour = 12
        self.min = 0
        self.sec = 0

        self.setWindowTitle('Time Setting')
        font = QFont('Arial', 20, QFont.Bold)
        self.time_label = QLabel(self)
        self.time_label.setFont(font)
        self.time_label.setText("SYSTEM TIME SETTING")
        self.time_label.setStyleSheet("background: white;")

        self.hour_btn_up = QPushButton('UP')
        self.hour_btn_down = QPushButton('DOWN')

        self.hour_label = QLabel(self)
        self.hour_label.setFont(font)
        self.hour_label.setText(str(12))

        self.colon_label = QLabel(self)
        self.colon_label.setFont(font)
        self.colon_label.setText(':')

        self.min_btn_up = QPushButton('UP')
        self.min_btn_down = QPushButton('DOWN')

        self.min_label = QLabel(self)
        self.min_label.setFont(font)
        self.min_label.setText(str(00))

        self.colon_label2 = QLabel(self)
        self.colon_label2.setFont(font)
        self.colon_label2.setText(':')

        self.sec_btn_up = QPushButton('UP')
        self.sec_btn_down = QPushButton('DOWN')

        self.second_label = QLabel(self)
        self.second_label.setFont(font)
        self.second_label.setText(str(00))

        self.hour_btn_up.clicked.connect(self.hour_btn_up_pressed)
        self.hour_btn_down.clicked.connect(self.hour_btn_down_pressed)
        self.min_btn_up.clicked.connect(self.min_btn_up_pressed)
        self.min_btn_down.clicked.connect(self.min_btn_down_pressed)
        self.sec_btn_up.clicked.connect(self.sec_btn_up_pressed)
        self.sec_btn_down.clicked.connect(self.sec_btn_down_pressed)

        self.use_sys_clk_btn = QPushButton('Use System Clock')
        self.complete_time_set_btn = QPushButton('Complete Time Setting')

        self.use_sys_clk_btn.clicked.connect(self.use_sys_clk_btn_pressed)
        self.complete_time_set_btn.clicked.connect(self.complete_time_set_btn_pressed)


        v_box = QVBoxLayout()
        v_box.addWidget(self.time_label)
        v_1_box = QVBoxLayout()
        v_1_box.addWidget(self.hour_btn_up)
        v_1_box.addWidget(self.hour_label)
        v_1_box.addWidget(self.hour_btn_down)
        v_2_box = QVBoxLayout()
        v_2_box.addWidget(self.min_btn_up)
        v_2_box.addWidget(self.min_label)
        v_2_box.addWidget(self.min_btn_down)
        v_3_box = QVBoxLayout()
        v_3_box.addWidget(self.sec_btn_up)
        v_3_box.addWidget(self.second_label)
        v_3_box.addWidget(self.sec_btn_down)
        h_1_box =  QHBoxLayout()
        h_1_box.addLayout(v_1_box)
        h_1_box.addWidget(self.colon_label)
        h_1_box.addLayout(v_2_box)
        h_1_box.addWidget(self.colon_label2)
        h_1_box.addLayout(v_3_box)
        h_2_box = QHBoxLayout()
        h_2_box.addWidget(self.use_sys_clk_btn)
        h_2_box.addWidget(self.complete_time_set_btn)
        v_box.addLayout(h_1_box)
        v_box.addLayout(h_2_box)

        self.setLayout(v_box)

    def hour_btn_up_pressed(self):
        self.hour += 1
        if self.hour > 24:
            self.hour = 0
        self.hour_label.setText(str(self.hour))

    def hour_btn_down_pressed(self):
        self.hour -= 1
        if self.hour < 0:
            self.hour = 23
        self.hour_label.setText(str(self.hour))

    def min_btn_up_pressed(self):
        self.min += 1
        if self.min > 60:
            self.min = 0
        self.min_label.setText(str(self.min))

    def min_btn_down_pressed(self):
        self.min -= 1
        if self.min < 0:
            self.min = 59
        self.min_label.setText(str(self.min))

    def sec_btn_up_pressed(self):
        self.sec += 1
        if self.sec > 60:
            self.sec = 0
        self.second_label.setText(str(self.sec))

    def sec_btn_down_pressed(self):
        self.sec -= 1
        if self.sec < 0:
            self.sec = 59
        self.second_label.setText(str(self.sec))

    def use_sys_clk_btn_pressed(self):
        self.time_packet.hour = 0
        self.time_packet.min = 0 
        self.time_packet.second = 0 
        self.time_packet.sys_clock  = True
        self.time_signal.emit(self.time_packet)
        self.close()

    def complete_time_set_btn_pressed(self):
        self.time_packet.hour = self.hour
        self.time_packet.min = self.min 
        self.time_packet.second = self.sec
        self.time_packet.sys_clock  = False
        self.time_signal.emit(self.time_packet)
        self.close()
