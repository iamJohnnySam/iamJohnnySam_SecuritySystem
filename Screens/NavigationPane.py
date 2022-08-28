from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import QSize

widgetsNavigation = {"Overview": [],
					 "Security": [],
					 "Solar": [],
					 "Alarms": [],
					 "Information": []}

def addButton(btnName):
	btn = QPushButton(btnName)
	btn.setFixedSize(QSize(150, 100))
	btn.setContentsMargins(50,0,50,0)
	return btn

def createNavigationPane():
	layout = QHBoxLayout()

	widgetsNavigation["Overview"].append(addButton('Overview'))
	widgetsNavigation["Security"].append(addButton('Security'))
	widgetsNavigation["Solar"].append(addButton('Solar Monitoring'))
	widgetsNavigation["Alarms"].append(addButton('Alarms'))
	widgetsNavigation["Information"].append(addButton('Information'))

	layout.addWidget(widgetsNavigation["Overview"][-1])
	layout.addWidget(widgetsNavigation["Security"][-1])
	layout.addWidget(widgetsNavigation["Solar"][-1])
	layout.addWidget(widgetsNavigation["Alarms"][-1])
	layout.addWidget(widgetsNavigation["Information"][-1])
	return layout