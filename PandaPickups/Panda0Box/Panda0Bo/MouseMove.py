from direct.showbase.ShowBase import ShowBase
from panda3d.core import Plane, Vec3, Point3, CardMaker
from panda3d.core import *
import Lt1

class Posrun(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        Lt1.run()   
        self.moselect=1
        
        self.cited=CollisionHandlerQueue()
        self.seleCollide=CollisionNode("SelectiMouse")
        self.selepath=camera.attachNewNode(self.seleCollide)
        self.seleray=CollisionRay()
        self.seleCollide.addSolid(self.seleray)
        
        self.selpan=CollisionTraverser()
        self.selpan.addCollider(self.selepath,self.cited)
        
        self.selectmo = loader.loadModel("EggMod/MailBoxing")

        self.selectmo.reparentTo(render)
        taskMgr.add(self.selectstart, "MouseMoving")
        self.accept("enter",self.moviselect)

        self.selectmo=loader.loadModel("EggMod/Pancakes_N1")
        self.selectmo.reparentTo(render)


    def moviselect(self):
        if self.moselect==1:
            self.moselect=0
        elif self.moselect==0:
            self.moselect=1

    def selectstart(self,task):
        if self.moselect==1:
            self.setSelectPos()
            
        return task.again
        

    def setSelectPos(self):
        try:
            self.selemo=base.mouseWatcherNode.getMouse()
            self.seleray.setFromLens(base.camNode,self.selemo.getX(),self.selemo.getY())
            self.selectmo.setCollideMask(CollideMask.allOff())
            self.selpan.traverse(render)
            if self.cited.getNumEntries()>0:
                self.cited.sortEntries()
                self.movecoll=self.cited.getEntry(0)
                print(self.movecoll.getSurfacePoint(render))
                self.selectmo.setPos(self.movecoll.getSurfacePoint(render))
                self.selectmo.setCollideMask(CollideMask.allOn())
                    
        except:
            pass
           
#SelectMoving=Posrun()
#SelectMoving.run()