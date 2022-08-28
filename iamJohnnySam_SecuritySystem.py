import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from Screens.TitlePane import createTitlePane
from Screens.NavigationPane import createNavigationPane

import logging
from datetime import datetime
logging.basicConfig(filename="log"+datetime.now().strftime("%Y%m%d-%H%M%S")+".log", encoding='utf-8', level=logging.INFO)
logging.info('System Started')

app = QApplication (sys.argv)
app.setStyle('Fusion')

windowMain = QWidget ()
windowMain.setWindowTitle ("iamJohnnySam Raspberry Pi Security & Monitoring System")

# Setting main layout
layoutMain = QVBoxLayout()
layoutMain.addLayout(createTitlePane(), 1)
layoutMain.addWidget(QPushButton('Placeholder'), 8)
layoutMain.addLayout(createNavigationPane(), 1)


windowMain.setLayout(layoutMain)

windowMain.show()
sys.exit(app.exec())