import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication (sys.argv)
windowMain = QWidget()
windowMain.setWindowTitle("iamJohnnySam Security System")

windowMain.show()
sys.exit(app.exec())