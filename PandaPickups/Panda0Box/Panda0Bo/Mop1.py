from direct.actor.Actor import Actor
import time
from panda3d.core import KeyboardButton
from direct.stdpy import threading
from panda3d.core import LVector3


class ango():
    def __init__(self):
        self.panra=1
        self.pwa=KeyboardButton.ascii_key("w")
        self.sano=Actor("HailPar.egg",{"Anaib":"Sbig-Armsjin"})
        self.thago=threading.Thread(target=self.run)
        self.thago.start()
        self.sano.reparentTo(render)
        

    def run(self):
        while self.panra>0:
            if base.mouseWatcherNode.is_button_down(self.pwa):
                self.sano.setPos(self.sano.getPos()+LVector3(-.1,0,0))
                time.sleep(0.01)


runi=ango()




