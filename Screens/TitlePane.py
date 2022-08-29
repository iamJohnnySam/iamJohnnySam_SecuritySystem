from pickle import TRUE
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

widgetsTitle = {"Connection": [],
				"Header": [],
				"Notification": [],
				"btnLogout": [],
				"towerLamp": []}

def createLabelConnection ():
	lbl = QLabel("Connection Status")
	lbl.setFixedSize(QSize(200, 75))
	widgetsTitle["Connection"].append(lbl)

def createMainArea ():
	x = 600
	logoWidth = 50

	lbl = QLabel("iamJohnnySam")
	lbl.setFixedSize(QSize(x-logoWidth,logoWidth))
	lbl.setAlignment(Qt.AlignCenter)
	widgetsTitle["Header"].append(lbl)

	lbl = QLabel("Notification")
	lbl.setFixedSize(QSize(x,25))
	lbl.setAlignment(Qt.AlignCenter)
	widgetsTitle["Notification"].append(lbl)

	logo = QLabel()
	image = QPixmap("Screens/Images/logo.png")
	logo.setPixmap(image)
	logo.setAlignment(Qt.AlignCenter)
	logo.setFixedSize(QSize(logoWidth,logoWidth))
	logo.setScaledContents(1)

	lyt2 = QHBoxLayout()
	lyt2.addWidget(logo)
	lyt2.addWidget(widgetsTitle["Header"][-1])

	lyt1 = QVBoxLayout()
	lyt1.addLayout(lyt2)
	lyt1.addWidget(widgetsTitle["Notification"][-1])
	return lyt1

def createTitlePane():
	layout = QHBoxLayout()

	createLabelConnection ()

	layout.addWidget(widgetsTitle["Connection"][-1])
	layout.addLayout(createMainArea ())
	layout.addWidget(QPushButton('Placeholder'))
	layout.addWidget(QPushButton('Placeholder'))
	return layout