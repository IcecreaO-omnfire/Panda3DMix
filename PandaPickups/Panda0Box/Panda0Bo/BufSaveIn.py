from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import CollideMask
from panda3d.core import *
from panda3d.physics import *
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import random
import sys
import os
import math
import LoadStar
import time

#sifpa=LoadStar.sifpa

class Pmango(PhysicsManager):
    def __init__(self):
        PhysicsManager.__init__(self)
        #        self.mopan=Pmango()
        
        #self.alin = LinearEulerIntegrator()
        #self.mopan.attachLinearIntegrator(self.alin)
        #self.arin = AngularEulerIntegrator()
        #self.mopan.attachAngularIntegrator(self.arin)
        
    
    
class Ites(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # This is used to store which keys are currently pressed.
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "back": 0, "up": 0}
        self.enpa=[]
        self.planey=[]
        self.planey.append(LoadStar.davplay())
        self.planey[0]["menm"]=LoadStar.loadRem("EggMod/BlastPow.egg")
        self.enpa.append(self.planey[0])
        

        taskMgr.add(self.taskpaint,"Carbe")

        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("arrow_down", self.setKey, ["back", True])
        self.accept("f", self.setKey, ["up", True])       
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])
        self.accept("arrow_down-up", self.setKey, ["back", False])
        self.accept("f-up", self.setKey, ["up", False]) 


    def taskpaint(self, task):
        for vpa in self.enpa:
            inu=time.clock()
            daet=vpa["clada"]
            cane={}
            for vab in vpa["frai"]:
                vab(locals())
                
            print(time.clock()-inu)
                
                
            for tenail in vpa["dam"]:
                tenail()
            
            
        return task.cont


    # Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection

    def move(self, task):
        # Get the time that elapsed since last frame.  We multiply this with
        # the desired speed in order to find out with which distance to move
        # in order to achieve that desired speed.
        dt = globalClock.getDt()
        self.dvi+=dt
        self.anr=self.an.getPhysicsObject()

        #print(self.anr.getVelocity())

        if dt<=.2:
            self.mopan.doPhysics(dt)
    
        if self.keyMap["left"]:
            self.movint.setH(self.movint.getH() + 200 * dt)
        if self.keyMap["right"]:
            self.movint.setH(self.movint.getH() - 200 * dt)
        if self.keyMap["forward"]:
            self.movint.setFluidY(self.movint, -25 * dt)          
        if self.keyMap["back"]:
            self.movint.setFluidY(self.movint, 25 * dt)
        if self.keyMap["up"]:
            self.movint.setFluidZ(self.movint, 25 * dt)

        # Normally, we would have to call traverse() to check for collisions.
        # However, the class ShowBase that we inherit from has a task to do
        # this for us, if we assign a CollisionTraverser to self.cTrav.
        #self.cTrav.traverse(render)
        

        return task.cont




    
simi=Ites()
simi.run()