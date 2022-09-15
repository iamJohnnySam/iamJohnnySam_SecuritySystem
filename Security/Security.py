from .CCTVEmailManager import CCTVEmailManager

class Security:
    def __init__ (self):
        self.CCTV = CCTVEmailManager('Security')
        self.CCTV.runCCTV()