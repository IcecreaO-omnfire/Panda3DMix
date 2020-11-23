from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import *
from panda3d.core import *
from panda3d.physics import *
from direct.task import *
from direct.interval.IntervalGlobal import *
import math

class loadModel():
    def __init__(self,obstart,mod1):
        obstart[mod1]=loader.loadModel(mod1)
        self.obstart=obstart[mod1]
        obstart[mod1].reparentTo(render)

class SphereCollide(dict):
    def __init__(self,collide1):
        self["sphere1"]=collide1.getChild(0).getBounds()
        self["spherecenter"]=self["sphere1"].getCenter()
        self["sphereradius"]=self["sphere1"].getRadius()
        self["collisionNode"]=CollisionNode("SphereGenerated")
        self["collisionNode"].addSolid(CollisionSphere(self["spherecenter"],self["sphereradius"]))
        self["collisionPath"]=collide1.attachNewNode(self["collisionNode"])
        self["collisionPath"].show()
        
        

def setuplights(self):
    self["PandLight1"]=DirectionalLight("PandLight1")

    self["LightPath1"]=render.attachNewNode(self["PandLight1"])

    self["LightPath1"].setHpr(-18,-52,14)
    render.setLight(self["LightPath1"])
    
    self["PandLight2"]=DirectionalLight("PandLight2")

    self["LightPath2"]=render.attachNewNode(self["PandLight2"])

    self["LightPath2"].setHpr(-18,-180,14)
    render.setLight(self["LightPath2"])    

def damage(self):
    if self["Health"]>0:
        self["Health"]-=1
        print(self["Health"])
        #print(self)
    

    
class DamageClass(dict):
    def __init__(self):
        loadModel(self,"Models/Damaging")
        self["Damaging"]=self["Models/Damaging"]
        self["model"]=self["Damaging"]
        self["Health"]=4
        self["Events"]=DirectObject()
        self["Events"].accept("DamageArea",self.DamageEvent)

        self["CollideModel"]=SphereCollide(self["model"])["collisionPath"]
        self["CollideModel"].show()
        
    def DamageEvent(self,collideEntry,functionpart):
        if id(collideEntry.getIntoNode())==id(self["CollideModel"].node()) and collideEntry.getFromNodePath().getName()=="SphereSource":
            #print(id(collideEntry.getIntoNodePath()),id(self["CollideModel"]))
            #self["model"].setPos(self["model"],collideEntry.getSurfacePoint(render))
            functionpart(self)

class DamageSphere(dict):
    def __init__(self):
        loadModel(self,"Models/DamageFrom")
        self["DamageFrom"]=self["Models/DamageFrom"]
        self["DamageFrom"].setScale(2)
        self["sphere1"]=self["DamageFrom"].getChild(0).getBounds()
        self["spherecenter"]=self["sphere1"].getCenter()
        self["sphereradius"]=self["sphere1"].getRadius()
        self["collisionNode"]=CollisionNode("SphereSource")
        self["collisionNode"].addSolid(CollisionSphere(self["spherecenter"],self["sphereradius"]))
        self.Sphere=self["DamageFrom"].attachNewNode(self["collisionNode"])
        self.collisionDetector=CollisionTraverser()
        self.queue=CollisionHandlerQueue()
        self.collisionDetector.addCollider(self.Sphere,self.queue)
        self.Sphere.show()
        taskMgr.add(self.collidePart,"CollidePart")
    def collidePart(self,task):
        try:
            self.collisionDetector.traverse(render)
            if self.queue.getNumEntries()>0:
                collidelist=self.queue.getEntries()
                for each in collidelist:
                    #print(each)
                    messenger.send("DamageArea",[each,damage])
        except:
            pass
        return task.cont
        

class GRun(ShowBase,dict):    
    def __init__(self):
        ShowBase.__init__(self)
        setuplights(self)
        self["playerOne"]=DamageClass()
        self["playerTwo"]=DamageClass()
        self["playerTwo"]["model"].setPos(0,5,0)
        self["Damage1"]=DamageSphere()
        self["Damage1"]["DamageFrom"].setPos(0,2,0)
        self["Damage1"].collisionDetector.addCollider(self["playerOne"]["CollideModel"],self["Damage1"].queue)
        self["Damage1"].collisionDetector.addCollider(self["playerTwo"]["CollideModel"],self["Damage1"].queue)
        
              


def prsel(self,access):
    print(self[access])
        

        
        
QuadRun=GRun()
QuadRun.run()
