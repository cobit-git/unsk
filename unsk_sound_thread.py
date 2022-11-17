from PyQt5.QtCore import pyqtSignal, QThread
import time 
import numpy as np
import random

class UnskData:

    def __init__(self):
        self.sound = np.zeros(100)
        self.code = 0
        self.distance = 0
        self.angle = 0

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
            '''
            For sound signal flow in amin thread(unsk_sound_detector_raw.py)
            You can adjust flow speed to adjust below sleep time.
            '''
            time.sleep(0.01)
            self.count += 1
            if self.count > 1000: 
                self.signal_packet.code  =  random.randint(0, 3)
                self.signal_packet.distance = random.randint(50,130)
                self.signal_packet.angle = random.randint(0, 360)
                '''
                For sound detect case - every 10 second, this simulator sends sound detecting packet to main thread(unsk_sound_detector_raw.py).
                You can replace below random number generator with real sound digital data. 
                In self.sound_packet, sound is list variable containing fake sound data.
                '''
                for i in range(100):
                    self.signal_packet.sound[i] = random.randint(10, 90)
                self.sound_signal.emit(self.signal_packet)
                self.count = 0
            else:
                sound_common.pop(0)
                '''
                For colck display case - every 0.01 second, this simulator adds random number to self.sounf_packet.sound. 
                And sends packet to amin thread. You can change current sound number with real sound digital data. 
                '''
                sound_common.append(random.randint(10, 90))
                self.signal_packet.code  = 4
                
                for i in range(100):
                    self.signal_packet.sound[99-i] = sound_common[i]
                self.sound_signal.emit(self.signal_packet)


    def stop(self):
        self.run_flag = False
        self.wait()
