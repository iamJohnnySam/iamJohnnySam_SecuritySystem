import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from Screens.TitlePane import createTitlePane
from Screens.NavigationPane import createNavigationPane

app = QApplication (sys.argv)
app.setStyle('Fusion')

windowMain = QWidget ()
windowMain.setWindowTitle ("iamJohnnySam Raspberry Pi Security & Monitoring System")

# Setting main layout
layoutMain = QVBoxLayout()
layoutMain.addLayout(createTitlePane())
layoutMain.addWidget(QPushButton('Placeholder'))
layoutMain.addLayout(createNavigationPane())


windowMain.setLayout(layoutMain)

windowMain.show()
sys.exit(app.exec())