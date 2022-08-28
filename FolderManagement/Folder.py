import os

class Folder:

    def __instancecheck__(self, Location):
        for f in os.listdir(Location):
            self.foldersize = self.foldersize + os.path.getsize(os.path.join(Location, f))
        print("Current Folder size -", "{:,}".format(self.foldersize))

