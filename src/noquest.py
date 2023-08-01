from PyQt6 import QtCore, QtGui, QtWidgets
import PyQt6
import subprocess
import time
import os.path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 405)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 370, 241, 31))
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
        self.pushButton_2.pressed.connect(self.startquest)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 10, 91, 41))
        self.pushButton_3.pressed.connect(self.fixdriver)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 60, 91, 41))
        self.pushButton_4.pressed.connect(self.debugtool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 380, 251, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 330, 151, 41))
        self.pushButton_5.pressed.connect(self.autotroubleshoot)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 10, 281, 281))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(True)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 230, 71, 41))
        self.pushButton_7.pressed.connect(self.ChangeASW)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 261, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 261, 171))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 244, 201))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 241, 151))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 101, 20))
        self.radioButton.setObjectName("radioButton")
        A = self.radioButton.isChecked()
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 101, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 101, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 80, 101, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 120, 101, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 100, 101, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 170, 191, 31))
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 170, 191, 31))
        self.pushButton_6.pressed.connect(self.ReinstallOculus)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.pressed.connect(self.openmirror)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quest Troubleshooter"))
        self.label.setText(_translate("MainWindow", "Quest Troubleshooter"))
        self.pushButton.setText(_translate("MainWindow", "Stop Quest"))
        self.pushButton_2.setText(_translate("MainWindow", "Start  Quest"))
        self.pushButton_3.setText(_translate("MainWindow", "Fix  Drivers"))
        self.pushButton_4.setText(_translate("MainWindow", "Debug Tool"))
        self.pushButton_5.setText(_translate("MainWindow", "Auto Troubleshoot"))
        self.label_2.setText(_translate("MainWindow", "Recomended"))
        self.groupBox.setTitle(_translate("MainWindow", "Advanced"))
        self.pushButton_7.setText(_translate("MainWindow", "Apply"))
        self.groupBox_2.setTitle(_translate("MainWindow", "ASW Options"))
        self.radioButton.setText(_translate("MainWindow", "Auto"))
        self.radioButton_2.setText(_translate("MainWindow", "18Hz ASW"))
        self.radioButton_3.setText(_translate("MainWindow", "30Hz ASW"))
        self.radioButton_4.setText(_translate("MainWindow", "45Hz ASW"))
        self.radioButton_5.setText(_translate("MainWindow", "Off"))
        self.pushButton_6.setText(_translate("MainWindow", "Reinstall Oculus Software"))
        self.radioButton_6.setText(_translate("MainWindow", "Force 45Hz"))
        self.pushButton_8.setText(_translate("MainWindow", "Gather Logs"))
        self.pushButton_9.setText(_translate("MainWindow", "Mirror"))

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
        time.sleep(3.5)
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
                # do very basic things
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

    def ReinstallOculus(self):
        self.progressBar.setValue(0)
        # It needs to basically delete all the EXEs from the runtime and run the "fixer.exe" (the "fixer.exe" will add new EXEs)
        subprocess.Popen("net stop OVRService",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        time.sleep(2.34)
        self.progressBar.setValue(10)
        # Probably not the best way the to delete items and Oculus made the quest work only on windows so it will work
        subprocess.Popen("del /f /q C:\Program Files\Oculus\Support\oculus-runtime\OVRServer_x64.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        self.progressBar.setValue(30)
        time.sleep(3.24)
        subprocess.Popen("del /f /q C:\Program Files\Oculus\Support\oculus-runtime\OVRServiceLauncher.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        self.progressBar.setValue(50)
        time.sleep(2.11)
        subprocess.Popen("del /f /q C:\Program Files\Oculus\Support\oculus-runtime\OVRRedir.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        time.sleep(4.2)
        self.progressBar.setValue(70)
        subprocess.Popen("C:\Program Files\Oculus\Support\oculus-diagnostics\Fixer.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
    def openmirror(self):
        subprocess.Popen("C:\Program Files\Oculus\Support\oculus-diagnostics\OculusMirror.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
    def ChangeASW(self):
        if self.radioButton.isChecked() == True:
                f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "r+")
                f.truncate(0)
                f.write("server:asw.Auto")
                f.close()

        if self.radioButton_2.isChecked() == True:
                f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "r+")
                f.truncate(0)
                f.write("server:asw.Clock18")
                f.close()

        if self.radioButton_3.isChecked() == True:
                f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "r+")
                f.truncate(0)
                f.write("server:asw.Clock30")
                f.close()
             
        if self.radioButton_4.isChecked() == True:
                f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "r+")
                f.truncate(0)
                f.write("server:asw.Clock45")
                f.close()

        if self.radioButton_5.isChecked() == True:
                f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "r+")
                f.truncate(0)
                f.write("server:asw.Off")
                f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    g = os.path.isfile("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt")
    if g == True:
            print("Creating Command file...") # this does nothing but Python needed a command here
    else:
        subprocess.Popen("""takeown /F "C:\Program Files\Oculus\Support\oculus-diagnostics" /A /R""",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )

        f = open("C:\Program Files\Oculus\Support\oculus-diagnostics\CommandsforCLI.txt", "x")
        f.close()

    sys.exit(app.exec())
