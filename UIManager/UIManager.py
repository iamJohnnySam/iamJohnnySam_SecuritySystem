import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

class UIManager(QMainWindow):
    def __init__(self):
        super(UIManager, self).__init__()
        loadUi("UI/uiApplication.ui", self)
        #self.lblLogo.setText("<html><head/><body><p><img src=':/Images/logo.png' width='100' height='100'></p></body></html>")

        self.nav1.clicked.connect(self.btnSecurity)
        self.nav2.clicked.connect(self.btnWorkout)
        self.nav3.clicked.connect(self.btnGarden)
        self.nav4.clicked.connect(self.btnOther)
        self.nav5.clicked.connect(self.btnPower)

    def btnSecurity (self):
        self.enableNavButtons()
        self.nav1.setEnabled(False)
        self.lblTitle.setText("Security System")
        self.mainWidget.setCurrentIndex(0)


    def btnWorkout (self):
        self.enableNavButtons()
        self.nav2.setEnabled(False)
        self.lblTitle.setText("Workout Management System")
        self.mainWidget.setCurrentIndex(1)

    def btnGarden (self):
        self.enableNavButtons()
        self.nav3.setEnabled(False)
        self.lblTitle.setText("Gardening System")
        self.mainWidget.setCurrentIndex(2)

    def btnOther (self):
        self.enableNavButtons()
        self.nav4.setEnabled(False)
        self.lblTitle.setText("Other")
        self.mainWidget.setCurrentIndex(3)

    def btnPower (self):
        self.enableNavButtons()
        self.nav5.setEnabled(False)
        self.lblTitle.setText("Power Management System")
        self.mainWidget.setCurrentIndex(4)

    def enableNavButtons (self):
        self.nav1.setEnabled(True)
        self.nav2.setEnabled(True)
        self.nav3.setEnabled(True)
        self.nav4.setEnabled(True)
        self.nav5.setEnabled(True)


