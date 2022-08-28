import CCTVclassify
from ..Global.globalVariables import *
from ..FolderManagement import Folder
from emailViewer import *

class CCTV:
    def __init__ (self):
        self.classifier1 = CCTVclassify("/home/pi/CCTV/model1.tflite")
        self.classifier2 = CCTVclassify("/home/pi/CCTV/model2.tflite")

        self.downloadFolder = Folder(FolderCCTVImagesDownload)

    def run ():
        outlookConnect ()
        outlookGetCCTV ()