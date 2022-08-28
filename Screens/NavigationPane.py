from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import QSize

def addButton(btnName):
	btn = QPushButton(btnName)
	btn.setFixedSize(QSize(150, 100))
	btn.setContentsMargins(50,0,50,0)
	return btn

def createNavigationPane():
	layout = QHBoxLayout()
	layout.addWidget(addButton('Overview'))
	layout.addWidget(addButton('Security'))
	layout.addWidget(addButton('Solar Monitoring'))
	layout.addWidget(addButton('Alarms'))
	layout.addWidget(addButton('Information'))
	return layout