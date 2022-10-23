from PyQt5.QtCore import pyqtSignal, QThread
import time 
import numpy as np
import random

class UnskData:

    def __init__(self):
        self.sound = np.zeros(100)
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
        sound_common = []
        for i in range(100):
            sound_common.append(random.randint(10, 90))
        while self.run_flag:
            time.sleep(0.01)
            self.count += 1
            if self.count > 1000: 
                self.signal_packet.code  =  random.randint(0, 3)
                self.signal_packet.distance = random.randint(50,130)
                for i in range(100):
                    self.signal_packet.sound[i] = random.randint(10, 90)
                self.sound_signal.emit(self.signal_packet)
                self.count = 0
            else:
                sound_common.pop(0)
                sound_common.append(random.randint(10, 90))
                
                self.signal_packet.code  = 4
                for i in range(100):
                    self.signal_packet.sound[99-i] = sound_common[i]
                self.sound_signal.emit(self.signal_packet)


    def stop(self):
        self.run_flag = False
        self.wait()
