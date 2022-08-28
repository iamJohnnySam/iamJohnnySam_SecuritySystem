from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize, Qt

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

	lbl = QLabel("iamJohnnySam")
	lbl.setFixedSize(QSize(x,50))
	lbl.setAlignment(Qt.AlignCenter)
	widgetsTitle["Header"].append(lbl)

	lbl = QLabel("Notification")
	lbl.setFixedSize(QSize(x,25))
	lbl.setAlignment(Qt.AlignCenter)
	widgetsTitle["Notification"].append(lbl)

	lyt = QVBoxLayout()
	lyt.addWidget(widgetsTitle["Header"][-1])
	lyt.addWidget(widgetsTitle["Notification"][-1])
	return lyt

def createTitlePane():
	layout = QHBoxLayout()

	createLabelConnection ()

	layout.addWidget(widgetsTitle["Connection"][-1])
	layout.addLayout(createMainArea ())
	layout.addWidget(QPushButton('Placeholder'))
	layout.addWidget(QPushButton('Placeholder'))
	return layout