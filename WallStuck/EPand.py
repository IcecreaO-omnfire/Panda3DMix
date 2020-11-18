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
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
import random
import sys
import os
import math

class A1():
    def __init__(self,ShowCon1):
        self.components=[]
        self.ShowCon1=ShowCon1
        #
        

class Pmango(PhysicsManager):
    def __init__(self):
        PhysicsManager.__init__(self)

class RA1(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.physicsMgr=Pmango()
        self.cTravA = CollisionTraverser()
        
        physicsMgr=self.physicsMgr
        
        self.alin = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(self.alin)
        self.arin = AngularEulerIntegrator()
        self.physicsMgr.attachAngularIntegrator(self.arin)
        
        alin = self.alin
        
        arin=self.arin
        
        
        grava=ForceNode('GravAll')
        grta=LinearVectorForce(0,0,-8)
        grava.addForce(grta)
        physicsMgr.addLinearForce(grta)
        self.readbuff=open("InterBuff.py","r+")
        
        self.taskMgr.add(self.phytime,"PhyTime")
        self.taskMgr.add(self.interbuff,"InterBuff")

        self.DinGro=CollisionHandlerQueue()
        #self.DinGro.setStaticFrictionCoef(1)
        #self.DinGro.setDynamicFrictionCoef(2)
        #self.DinGro.setAlmostStationarySpeed(0.1)
        
        

    def phytime(self,task):
        self.physicsMgr.doPhysics(.01)
        #Wait(1)
        return task.cont

    def interbuff(self,task):
        
        exec(self.readbuff.read(),globals())
        #self.readbuff.truncate(0)
        #self.readbuff.seek(0)
        return task.cont

        
        

class P1():
    
    def __init__(self,AreaIncluded):
        self.connect=[]
        self.connect.append(AreaIncluded)
        self.modstart=loader.loadModel("EggMod/Roblock3.egg")
        self.modstart.reparentTo(render)
        self.modact=ActorNode("P1ModAct")
        self.modcollide=CollisionSphere(0,0,-0,3)
        self.modcollision=CollisionNode("ModActCollision")
        self.modfri=self.modcollision.addSolid(self.modcollide)
        #self.modfri.node().attachNewNode(self.modcollision)
        
        self.modactIn=render.attachNewNode(self.modact)
        self.modactIn.node().getContactVector()
        self.modcollision=self.modactIn.attachNewNode(self.modcollision)
        self.modcollision.setPos(0,0,-0)
        self.modstart.setPos(0,0,3)
        self.modstart.reparentTo(self.modactIn)
        AreaIncluded.ShowCon1.physicsMgr.attachPhysicalNode(self.modactIn.node())
        #AreaIncluded.ShowCon1.DinGro.addCollider(self.modcollision,self.modact) #Colliders use nodepaths for collisions instead of nodes
        AreaIncluded.ShowCon1.cTravA.addCollider(self.modcollision, AreaIncluded.ShowCon1.DinGro)
        #Monolo
    

class P1OS1():
    #P1 Off Switch
    def __init__(self,P1Con):
        self.volume=None 
        self.P1=P1Con
        self.P1.connect.append(self) 

    def off(self):
        self.P1.modactIn.node().getPhysicsObject().setActive(False)
        self.P1.modcollision.setCollideMask(BitMask32.allOff())
        pass

    def disconnect(self):
        self.P1.connect.remove(self)

class P1OS2():
    #P1 On Switch
    def __init__(self,P1Con):
        self.P1=P1Con
        self.P1.connect.append(self) 
    def on(self):
        self.P1.modactIn.node().getPhysicsObject().setActive(True)
        self.P1.modcollision.setCollideMask(BitMask32.allOn())
 
class P2():
     #P1 Gravity Switch
    def __init__(self,P1Con):
         self.P1=P1Con
         self.P1.connect.append(self) 
         
    def disconnect(self):
        self.P1.connect.remove(self)

    def gravityon(self):
        grta.get_vector_masks().z=1
    
    def gravityoff(self):
        grta.get_vector_masks().z=0
         

class P3(DirectObject.DirectObject):
    
    def __init__(self,P1Con):
        self.P1=P1Con
        self.movingdirect = {
            "left": 0, "right": 0, "forward": 0, "back": 0, "up": 0}

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
        taskMgr.add(self.movesinput,"moving")
        self.P1.connect.append(self) 

        
    def setKey(self, key, value):
        self.movingdirect[key] = value
        
    def movesinput(self,task):
        if globalClock.getDt()<=.2:
            self.moving()
        #Wait(0.1)
        return task.cont
        
    def moving(self):
        dt = globalClock.getDt()
        if dt<=.2:            
            if self.movingdirect["left"]:
                self.P1.modactIn.setH(self.P1.modactIn.getH() + 200 * dt)
            if self.movingdirect["right"]:
                self.P1.modactIn.setH(self.P1.modactIn.getH() - 200 * dt)
            if self.movingdirect["forward"]:
                self.P1.modactIn.setFluidY(self.P1.modactIn,-25 * dt)          
            if self.movingdirect["back"]:
                self.P1.modactIn.setFluidY(self.P1.modactIn,25 * dt)
            if self.movingdirect["up"]:
                self.P1.modactIn.setZ(self.P1.modactIn,89 * dt)
            #self.P1.modstart.setPos(self.P1.modact.getRelativePoint(render,self.P1.modact.getPos()))
            #self.P1.modact.node().getPhysicsObject().addImpulse(LVector3(0,0,1953*dt))
        self.P1.connect[0].ShowCon1.cTravA.traverse(render)
        self.P1.modcollision.show()
        
        entries = list(self.P1.connect[0].ShowCon1.DinGro.getEntries())
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        #seta
        if len(entries) > 0:
            print(self.P1.modactIn.getPos())
            self.P1.modactIn.setZ(entries[0].getSurfacePoint(render).getZ())
            #print(self.P1.modactIn.node().getContactVector())
            print(entries[0].getSurfacePoint(render).getZ())
            print(self.P1.modactIn.getPos())
            print(self.P1.modactIn.getRelativePoint(render,self.P1.modactIn.getPos()))
            #print(self.P1.modcollision.getRelativePoint(render,self.P1.modcollision.getPos()))
            #self.P1.modcollision.setPos(self.P1.modact.getRelativePoint(self.P1.modact,entries[0].getSurfacePoint(render)+LVector3(0,0,1.5)))
            #self.P1.modact.setPos(self.P1.modcollision.getRelativePoint(render,entries[0].getSurfacePoint(render)))
            #self.P1.modstart.setPos(self.P1.modact.getRelativePoint(render,self.P1.modact.getPos()))
            quat = Quat()
            headsUp(quat,self.P1.modactIn.getQuat().getForward(),entries[0].getSurfaceNormal(render))
            self.P1.modactIn.setP(quat.getHpr()[1])
            self.mvel=self.P1.modactIn.node().getPhysicsObject().getVelocity()
            self.P1.modactIn.node().getPhysicsObject().setVelocity(self.mvel.x,self.mvel.y,0)




        
    def speedone(self):
        pass
    def speedtwo(self):
        pass
    
    def disconnect(self):
        self.ignoreAll()
        self.P1.connect.remove(self) 
WorldA=RA1()
Sect1=A1(WorldA)
hifi=P1(Sect1)
Sect1.components.append(hifi)
bop=P3(hifi)
WorldA.run()
