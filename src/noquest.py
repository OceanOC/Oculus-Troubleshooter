from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import PyQt6
import subprocess
import time
import os.path

oculuspath = os.getenv('OculusBase')
cmdpath = oculuspath+"Support\oculus-diagnostics\CommandsforCLI.txt"
ver = "1.3.0a"

class SettingsWindow(QWidget):
    global controllerdone
    controllerdone = False
    def setupUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 430, 71, 41))
        self.pushButton_7.pressed.connect(self.ApplyAdvancedSettings)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(0, 410, 661, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 141, 151))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 101, 20))
        self.radioButton.setObjectName("radioButton")
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
        self.radioButton_6.setGeometry(QtCore.QRect(20, 100, 111, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 10, 191, 41))
        self.pushButton_6.pressed.connect(self.ReinstallOculus)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Advanced Settings"))
        self.pushButton_7.setText(_translate("Form", "Apply"))
        self.groupBox_2.setTitle(_translate("Form", "ASW Options"))
        self.radioButton.setText(_translate("Form", "Auto"))
        self.radioButton_2.setText(_translate("Form", "18Hz ASW"))
        self.radioButton_3.setText(_translate("Form", "30Hz ASW"))
        self.radioButton_4.setText(_translate("Form", "45Hz ASW"))
        self.radioButton_5.setText(_translate("Form", "Off"))
        self.radioButton_6.setText(_translate("Form", "Force 45Hz"))
        self.pushButton_12.setText(_translate("Form", "Performance HUD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Headset"))
        self.checkBox.setText(_translate("Form", "Disable Controller Sleep"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Controllers"))
        self.pushButton_6.setText(_translate("Form", "Reinstall Oculus Software"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Misc."))

    def ApplyAdvancedSettings(self):
            aswdone = False
            global controllerdone
            controllerdone = False
            if self.radioButton.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Auto")
                    f.close()
                    aswdone = True


            if self.radioButton_2.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Clock18\r\n")
                    f.close()
                    aswdone = True

            if self.radioButton_3.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Clock30\r\n")
                    f.close()
                    aswdone = True

            if self.radioButton_4.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Clock45\r\n")
                    f.close()
                    aswdone = True

            if self.radioButton_5.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Off\r\n")
                    f.close()
                    aswdone = True

            if self.radioButton_6.isChecked() == True:
                    aswdone = False
                    f = open(cmdpath, "r+")
                    f.truncate(0)
                    f.write("server:asw.Sim45\r\n")
                    f.close()
                    aswdone = True

            if self.checkBox.isChecked() == True and aswdone == True:
                    controllerdone = False
                    f = open(cmdpath, "a+")
                    f.write("server:Touch.DisableSleep true\r\n")
                    f.close()
                    controllerdone = True

            if self.checkBox.isChecked() == False and aswdone == True:
                    controllerdone = False
                    f = open(cmdpath, "a+")
                    f.write("server:Touch.DisableSleep false\r\n")
                    f.close()
                    controllerdone = True

    def ReinstallOculus(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Are you sure?")
        dlg.setText("""Are you sure you want to reinstall Oculus? \r\n If yes, press the Repair button on the next window""")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
                  subprocess.Popen(oculuspath+"OculusSetup.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        else:
            print("")
    

    def pHUD(self):
            global perfdone
            perfdone = False
            f = open(cmdpath, "a+")
            f.write("perfhud\r\n")
            f.close()
            perfdone = True
          

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 405)
        MainWindow.setFixedSize(499, 405)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
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
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.stopquest)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.pushButton_2.pressed.connect(self.startquest)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 20, 91, 31))
        self.pushButton_3.pressed.connect(self.FixDriver)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 60, 91, 31))
        self.pushButton_4.pressed.connect(self.DebugTool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 380, 251, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.pressed.connect(self.openmirror)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 340, 151, 31))
        self.pushButton_10.pressed.connect(self.OpenFolder)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(170, 340, 151, 31))
        self.pushButton_11.pressed.connect(self.OpenAdvancedSettings)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 271, 41))
        self.label_3.setHidden(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oculus Troubleshooter"))
        self.label.setText(_translate("MainWindow", "Oculus Troubleshooter"))
        self.pushButton.setText(_translate("MainWindow", "Stop Oculus"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Oculus"))
        self.pushButton_3.setText(_translate("MainWindow", "Fix  Drivers"))
        self.pushButton_4.setText(_translate("MainWindow", "Debug Tool"))
        self.pushButton_8.setText(_translate("MainWindow", "Gather Logs"))
        self.pushButton_9.setText(_translate("MainWindow", "Mirror"))
        self.pushButton_10.setText(_translate("MainWindow", "Open Oculus folder"))
        self.pushButton_11.setText(_translate("MainWindow", "Advanced  Settings"))
        self.label_3.setText(_translate("MainWindow", "(Oculus Restart Required)"))

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
        self.label_3.setHidden(True)
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

    def openmirror(self):
          subprocess.Popen(oculuspath+"Support\oculus-diagnostics\OculusMirror.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )

    def FixDriver(self):
        self.progressBar.setValue(0)
        subprocess.Popen(oculuspath+"Support\oculus-drivers\oculus-driver.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )
        self.progressBar.setValue(50)
        time.sleep(3.6)
        self.progressBar.setValue(100)
        
    def DebugTool (self):
                subprocess.Popen(oculuspath+"Support\oculus-diagnostics\OculusDebugTool.exe",
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )

    def OpenFolder(self):
                  subprocess.Popen("explorer "+oculuspath,
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE,
                         text = True,
                         shell = True
                         )

    def OpenAdvancedSettings(self):
        self.Form = QtWidgets.QWidget()
        self.w = SettingsWindow(self.Form)
        self.w.setupUI(self.Form)
        self.w.show()
        self.Form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    g = os.path.isfile(cmdpath)
    if g == True:
            print("Command file already created") # this does nothing but Python needed a command here
    else:
        print("Command file creating...")
        subprocess.Popen("""takeown /F " """+oculuspath+""" " /R""",
                         stdout = sys.stdout, 
                         stderr = sys.stdout,
                         text = True,
                         shell = True,
                         )
        
        subprocess.Popen("""ICACLS " """+oculuspath+""" " /grant "Administrators":F""",
                         stdout = sys.stdout, 
                         stderr = sys.stdout,
                         text = True,
                         shell = True,
                         )

        f = open(cmdpath, "x")
        f.close()

    sys.exit(app.exec())
