from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.physics import *
from direct.task import *
import math
from direct.gui.OnscreenText import *

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
        
def collisionsetup(self):
    self["CollisionEvent"].addInPattern("into-%in")
    self["SphereBall"]=SphereCollide(self["Basketball"])["collisionPath"]
    self["SphereBall"].reparentTo(self["Basketball"])
    self["HoopBasket"]=CollisionNode("Sphere1")
    self["HoopBasket"].addSolid(CollisionSphere(0,0,0,0.5))

    self["HoopPath"]=render.attachNewNode(self["HoopBasket"])
    self["HoopPath"].reparentTo(self["HoopBall"])
    self["HoopPath"].setPos(self["HoopBall"].find("**/HoopSpace").getPos())
    self["HoopBall"].find("**/HoopSpace").setTransparency(TransparencyAttrib.MAlpha)
    self["HoopBall"].find("**/HoopSpace").setAlphaScale(0)
    

    base.cTrav.addCollider(self["SphereBall"],self["CollisionEvent"])
    base.cTrav.addCollider(self["HoopPath"],self["CollisionEvent"])

def setuplights(self):
    self["PandLight1"]=DirectionalLight("PandLight1")

    self["LightPath1"]=render.attachNewNode(self["PandLight1"])

    self["LightPath1"].setHpr(-18,-52,14)
    render.setLight(self["LightPath1"])
    
    self["PandLight2"]=DirectionalLight("PandLight2")

    self["LightPath2"]=render.attachNewNode(self["PandLight2"])

    self["LightPath2"].setHpr(-18,-180,14)
    render.setLight(self["LightPath2"])    


    
def Collide(self,entry):
    self["textUp"].text=str(int(self["textUp"].text)+1)
    
class GRun(ShowBase,dict):

    def projectilestrength(self,task):
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.control()):
            self["ProjectStrength"]+=self["ProjectDirection"]
            print(self["ProjectStrength"])
            if self["ProjectStrength"]>=10:
                self["ProjectDirection"]*=-1
            elif self["ProjectStrength"]<=0:
                self["ProjectDirection"]*=-1
            self["ProjectDown"]=1
        elif not base.mouseWatcherNode.isButtonDown(KeyboardButton.control()):
            if self["ProjectDown"]==1:
                self["Basketball"].reparentTo(render)
                self["Basketball"].setZ(self["PenguiBall"].getZ())
                self["Basketball"].setPos(self["PenguiBall"],0,0.1,0)
                projectile.strength=self["ProjectStrength"]
                projectile.status=0
                projectile.z=self["Basketball"].getZ()
                projectile.forwardball = render.getRelativeVector(self["PenguiBall"],(0,1,0))
                #taskMgr.doMethodLater(0.01,projectile,"ProjectTraject",extraArgs=[self],appendTask=True)
                #Adding the method to the task manager will be called every time this function is called
                taskMgr.doMethodLater(0.01,projectile,"ProjectTraject",extraArgs=[self],appendTask=True)
                self["ProjectDown"]=0
        return task.again
    
    def __init__(self):
        ShowBase.__init__(self)
        self["ProjectDown"]=0
        self["ProjectDirection"]=0.1
        self["ProjectStrength"]=0                                                                   
        self["textUp"]=OnscreenText(text="0",pos=(1,0),scale=0.5,mayChange=True)
        base.cTrav=CollisionTraverser()
        self["CollisionEvent"]=CollisionHandlerEvent()
        #A collision traverser named cTrav is called automatically
        loadModel(self,"CanyonBask")
        loadModel(self,"PenguiBall")
        loadModel(self,"HoopBall")
        loadModel(self,"Basketball")
        base.camera.reparentTo(self["PenguiBall"])
        self["Basketball"].setScale(0.05)
        self["PenguiBall"].setScale(0.05)
        self["HoopBall"].setScale(0.3)
        self["HoopBall"].setPos(-2,-20,7.6)
        self["HoopBall"].setH(180)
        self["PenguiBall"].setPos(-2,-18,7.6)
        collisionsetup(self)
        setuplights(self)

        taskMgr.doMethodLater(0.01,PenMove,"PenMove",extraArgs=[self],appendTask=True)
        self.accept("into-Sphere1",Collide,extraArgs=[self])
        self.camLens.setFov(120)
        self["HoopPath"].show()
        self["SphereBall"].show()
        taskMgr.doMethodLater(0.01,self.projectilestrength,"ProjectLaunch")

def projectile(self,task):
    a=-8.0
    b=10
    c=0.0
    
    if projectile.status<1 or self["Basketball"].getZ()>0:
        z=a*(projectile.status)**2+b*(projectile.status)+c
        #print(self["ProjectStrength"])
        self["Basketball"].setPos(self["Basketball"],projectile.forwardball*self["ProjectStrength"])
        #print(projectile.forwardball)
        self["Basketball"].setZ(projectile.z+z)
        projectile.status+=0.01
    else:
        return task.done
    return task.again

        
    
def PenMove(self,task):
        base.cTrav.traverse(render)
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.asciiKey("w")):
            self["PenguiBall"].setPos(self["PenguiBall"],(0,0.1,0))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.asciiKey("a")):
            self["PenguiBall"].setPos(self["PenguiBall"],(-0.1,0,0))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.asciiKey("d")):
            self["PenguiBall"].setPos(self["PenguiBall"],(0.1,0,0))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.asciiKey("s")):
            self["PenguiBall"].setPos(self["PenguiBall"],(0,-0.1,0))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.enter()):
            self["PenguiBall"].setPos(self["PenguiBall"],(0,0,1))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.shift()):
            self["PenguiBall"].setPos(self["PenguiBall"],(-0,0,-1))
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.right()):
            self["PenguiBall"].setH(self["PenguiBall"],-1)
        if base.mouseWatcherNode.isButtonDown(KeyboardButton.left()):
            self["PenguiBall"].setH(self["PenguiBall"],1)


        return task.again        


def prsel(self,access):
    print(self[access])
        

        
        
QuadRun=GRun()
QuadRun.run()
