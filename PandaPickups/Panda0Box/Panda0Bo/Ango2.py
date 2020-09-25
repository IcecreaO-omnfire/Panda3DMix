from direct.actor.Actor import Actor
from panda3d.core import *
import random
class angob():
    def __init__(self):
        self.sano=Actor("EggMod/Roblock1.egg",{"BB1":"EggMod/Roblock1-WB1.egg","BB2":"EggMod/Roblock3-A2.egg"})
        self.sano.makeSubpart("LWalk", ["Bone.006","Bone.007","Bone.008","Bone.009"],
        ["Bone.001","Bone.002","Bone.010","Bone.011"])
        self.sano.makeSubpart("LYou", ["Bone.001","Bone.002","Bone.010","Bone.011"],
        ["Bone.006","Bone.007","Bone.008","Bone.009"])
        self.sano.reparentTo(render)
        self.sano.setTexture(loader.loadTexture("tex/M6.png"))

            
        
    

runi=angob()

runi.sano.loop("BB1",partName="LWalk")
runi.sano.loop("BB2",partName="LYou")

