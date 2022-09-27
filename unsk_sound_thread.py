from PyQt5.QtCore import pyqtSignal, QThread
import time 
import numpy as np
import random

class UnskData:

    def __init__(self):
        self.sound = np.empty(100)
        self.code = 0
        self.distance = 0

class SoundDetector(QThread):

    signal_packet = UnskData()
    sound_signal= pyqtSignal(UnskData)

    def __init__(self):
        super().__init__()
        self.run_flag = True
        self.count = 0
        

    def run(self):
        while self.run_flag:
            time.sleep(1)
            self.count += 1
            if self.count > 10: 
                print("10 second timer")
                self.signal_packet.code  = 0 #random.randint(0,3)
                self.signal_packet.distance = random.randint(50, 130)
                self.sound_signal.emit(self.signal_packet)
                self.count = 0

    def stop(self):
        self.run_flag = False
        self.wait()
