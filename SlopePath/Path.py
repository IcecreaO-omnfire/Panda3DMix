from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import Lt1

def acceptmechanics(self):
 self.accept("a-repeat",self.amo1)
 self.accept("d-repeat",self.amo2)
 self.accept("w-repeat",self.amo3)
 self.accept("s-repeat",self.amo4) 

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        Lt1.run()
        self.cTravA=CollisionTraverser()
        self.collisionprocess=CollisionHandlerQueue()
        f=loader.loadModel("Bri3.egg")
        f.reparentTo(render)
        f.setScale(20)
        self.a=loader.loadModel("Roblock3_I.egg")
        self.a.reparentTo(render)
        self.a.setPos(0,0,5)
        self.a.setScale(1)
        acceptmechanics(self)
        o=CollisionNode("CollideA")
        o.addSolid(CollisionSphere(0,0,-0,3))
        o=self.a.attachNewNode(o)
        self.cTravA.addCollider(o,self.collisionprocess)
        o.show()
        taskMgr.add(self.collision1,"CollisionDetect")
        #f.removeNode()
        self.useTrackball()
    def collision1(self,task):
        self.cTravA.traverse(render)
        collide1=self.collisionprocess.getEntries()
        if len(collide1)>0:
         self.po=self.a.getPos()
         self.a.setPos(self.po.x,self.po.y,collide1[0].getSurfacePoint(render).getZ()+3)
         #quat = Quat()
         self.a.headsUp(self.a.getQuat().getForward(),collide1[0].getSurfaceNormal(render))
         print(self.a.getQuat().getForward())
         #self.a.setP(quat.getHpr()[1])
         #print(self.a.getP())
        return task.cont
        
    def amo1(self):
     self.a.setPos(self.a,-1,0,0)
    def amo2(self):
     self.a.setPos(self.a,1,0,0)
    def amo3(self):
     self.a.setPos(self.a,0,1,0)
    def amo4(self):
     self.a.setPos(self.a,0,-1,0)

App().run()