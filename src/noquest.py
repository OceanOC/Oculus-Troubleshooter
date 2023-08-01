from PyQt6 import QtCore, QtGui, QtWidgets
import PyQt6
import subprocess
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 337)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 280, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(7)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 290, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Cabin")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.stopquest)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.pushButton.pressed.connect(self.startquest)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 60, 91, 41))
        self.pushButton_4.pressed.connect(self.debugtool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 260, 221, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 210, 151, 41))
        self.pushButton_5.pressed.connect(self.autotroubleshoot)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quest troubleshooter"))
        self.pushButton.setText(_translate("MainWindow", "Stop Quest"))
        self.pushButton_2.setText(_translate("MainWindow", "Start  Quest"))
        self.pushButton_3.setText(_translate("MainWindow", "Fix  Drivers"))
        self.pushButton_4.setText(_translate("MainWindow", "Debug Tool"))
        self.pushButton_5.setText(_translate("MainWindow", "Auto Troubleshoot"))

    def startquest(self):
        self.progressBar.setValue(0)
        time.sleep(2)
        self.progressBar.setValue(50)
        subprocess.Popen("net start OVRService",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        time.sleep(6)
        self.progressBar.setValue(100)
        
    def stopquest(self):
        self.progressBar.setValue(0)
        time.sleep(4.1)
        self.progressBar.setValue(50)
        subprocess.Popen("net stop OVRService",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        time.sleep(2.56)
        self.progressBar.setValue(100)

    def fixdriver(self):
        self.progressBar.setValue(0)
        subprocess.Popen("C:\Program Files\Oculus\Support\oculus-drivers\oculus-driver.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        self.progressBar.setValue(50)
        time.sleep(3.6)
        self.progressBar.setValue(100)
        
    def debugtool (self):
                subprocess.Popen("C:\Program Files\Oculus\Support\oculus-diagnostics\OculusDebugTool.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
                
    def autotroubleshoot(self):
                self.progressBar.setValue(0)
                subprocess.Popen("net stop OVRService",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
                self.progressBar.setValue(30)
                time.sleep(3.1)
                subprocess.Popen("net start OVRService",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
                self.progressBar.setValue(60)
                time.sleep(5.3)
                subprocess.Popen("C:\Program Files\Oculus\Support\oculus-drivers\oculus-driver.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
                self.progressBar.setValue(100)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
