from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import time
class Magip(ShowBase):
    def __init__(self):
            sap=time.clock()
            ShowBase.__init__(self)
            sap=time.clock()-sap
            print(sap)		

print("Magip")

