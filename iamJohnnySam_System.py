import sys
import logging
from datetime import datetime
from PyQt5.QtWidgets import QApplication

import Garden, Security, Power, Workout

from UI.uiManager import *

### Event Logging
logging.basicConfig(filename="log"+datetime.now().strftime("%Y%m%d-%H%M%S")+".log", encoding='utf-8', level=logging.INFO)
logging.info('System Started')

sec = Security()
gar = Garden()
wor = Workout()
pwr = Power()

def runUI():
    app = QApplication (sys.argv)
    app.setStyle('Fusion')
    window = UIApp()
    window.show()
    sys.exit(app.exec())

runUI()