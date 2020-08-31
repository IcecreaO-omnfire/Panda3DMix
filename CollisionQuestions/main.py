#!/usr/bin/env python

from panda3d.core import *
# Tell Panda3D to use OpenAL, not FMOD
loadPrcFileData("", "audio-library-name p3openal_audio")

from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import *


class CollisionPARun(ShowBase):

    def __init__(self):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)
        self.GroundStand=loader.loadModel("GroundPin.egg")
        self.GroundStand.reparentTo(render)
        self.nt=0
        self.downw=KeyboardButton.ascii_key('w')
        self.downs=KeyboardButton.ascii_key("s")
        self.downa=KeyboardButton.asciiKey("a")
        self.downd=KeyboardButton.asciiKey("d")
        self.keyplace=base.mouseWatcherNode.is_button_down
        self.cTrav=CollisionTraverser()
        self.QueueCollisions = CollisionHandlerQueue()
        self.MovePlace=loader.loadModel("camera.egg")
        self.MovePlace.reparentTo(render)
        self.collide=CollisionNode("CollideNode")
        self.collide=self.MovePlace.attachNewNode(self.collide)
        self.he=CollisionSphere(0, 0, -2.0, 1)
        self.collide.node().addSolid(self.he)
        self.collide.show()
        self.MovePlace.show()
        self.cTrav.addCollider(self.collide,self.QueueCollisions)
        self.cTrav.showCollisions(render)
        taskMgr.add(self.PCMove,"PMTop")
        taskMgr.add(self.CollideProcess,"C1")
        
    
    def CollideProcess(self,task):
        epa=self.QueueCollisions.getEntries()
        if len(epa)>0:
            epa=epa[0]
            self.MovePlace.setPos(epa.getSurfacePoint(render)+LVector3(0,0,3))
        
            
        return task.cont
    
    def PCMove(self,task):
        if self.nt==0:
            self.nt=1
            if self.keyplace(self.downw):
                self.MovePlace.setPos(self.MovePlace,1,0,0)
                #Wait(1.2)
            if self.keyplace(self.downs):
                self.MovePlace.setPos(self.MovePlace,-1,0,0)
                #Wait(1.2)
                
            if self.keyplace(self.downa):
                self.MovePlace.setPos(self.MovePlace,0,0,1)
                #Wait(1.2)
            
            if self.keyplace(self.downd):
                self.MovePlace.setPos(self.MovePlace,0,-0,-1)
                #Wait(1.2)
            
        elif self.nt==1:
            Wait(1.2)
            self.nt=0
            
            
        return task.cont


collisionvolley = CollisionPARun()
collisionvolley.run()
