import sys
import logging
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from Screens.TitlePane import *
from Screens.InformationPane import *
from Screens.NavigationPane import *

### Event Logging
logging.basicConfig(filename="log"+datetime.now().strftime("%Y%m%d-%H%M%S")+".log", encoding='utf-8', level=logging.INFO)
logging.info('System Started')

widgetsMain = {"Title": [],
               "Information": [],
               "Navigation": []}

app = QApplication (sys.argv)
app.setStyle('Fusion')

### Main Window settings
windowMain = QWidget ()
windowMain.setWindowTitle ("iamJohnnySam Raspberry Pi Security & Monitoring System")
windowMain.setFixedWidth(1500)
windowMain.setFixedHeight(800)
# windowMain.setStyleSheet("background: #161219;")

### Setting main layout
layoutMain = QVBoxLayout()

TitlePane = createTitlePane()
widgetsMain["Title"].append(TitlePane)
NavigationPane = createNavigationPane()
widgetsMain["Navigation"].append(NavigationPane)

layoutMain.addLayout(widgetsMain["Title"][-1], 1)
layoutMain.addWidget(QPushButton('Placeholder'), 8)
layoutMain.addLayout(widgetsMain["Navigation"][-1], 1)

windowMain.setLayout(layoutMain)

windowMain.show()
sys.exit(app.exec())