import sys
import time
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt

numPoints=1000
xs=numpy.arange(numPoints)
ys=numpy.sin(3.14159*xs*10/numPoints) #this is our data

try:
    fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:
    def _fromUtf8(s):
    return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.index = 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_pulse = QtGui.QPushButton(Form)
        self.start_pulse.setObjectName(_fromUtf8("start_pulse"))
        self.stop_pulse = QtGui.QPushButton(Form)
        self.stop_pulse.setObjectName(_fromUtf8("stop_pulse"))
        self.horizontalLayout.addWidget(self.start_pulse)
        self.horizontalLayout.addWidget(self.stop_pulse)
        self.label = QtGui.QLabel(Form)
        self.label.setAutoFillBackground(True)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("GUI.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def refreshUi(self):
        if self.index%10==0:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/10.jpg")))
        if self.index%10==1:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/1.jpg")))
        if self.index%10==2:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/2.jpg")))
        if self.index%10==3:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/3.jpg")))
        if self.index%10==4:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/4.jpg")))
        if self.index%10==5:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/5.jpg")))
        if self.index%10==6:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/6.jpg")))
        if self.index%10==7:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/7.jpg")))
        if self.index%10==8:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/8.jpg")))
        if self.index%10==9:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/9.jpg")))

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.start_pulse.setText(_translate("Form", "start", None))
        self.start_pulse.clicked.connect(self.start)
        self.stop_pulse.setText(_translate("Form", "stop", None))
        self.stop_pulse.clicked.connect(self.stop)

    def start(self):
        self.timer1.start(500.0) #set the interval (in ms)

    def stop(self):
        self.timer1.stop() #stop the timer

    def change_index(self):
        self.index += 1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win_plot = Ui_Form()

    win_plot.index = 0
    win_plot.timer = QtCore.QTimer() #start a timer (to call replot events)
    win_plot.timer.start(100.0) #set the interval (in ms)
    win_plot.connect(win_plot.timer, QtCore.SIGNAL('timeout()'), win_plot.refreshUi)

    win_plot.timer1 = QtCore.QTimer() #start a timer (to call replot events)
    win_plot.connect(win_plot.timer1, QtCore.SIGNAL('timeout()'),
        win_plot.change_index)

    # show the main window
    win_plot.show()
sys.exit(app.exec_())