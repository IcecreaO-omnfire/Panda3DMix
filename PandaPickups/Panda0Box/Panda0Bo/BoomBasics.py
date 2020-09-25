from direct.showbase.InputStateGlobal import inputState
from direct.showbase.ShowBase import *
from panda3d.core import *

from panda3d.bullet import *


class BoomerBasic(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        
        sepand1=DirectionalLight("sela")
        
        mas=render.attachNewNode(sepand1)

        mas.setHpr(-18,-52,14)
        render.setLight(mas)

        taskMgr.add(self.update, 'updateWorld') 
        
        self.setup()
        
        self.st=self.sm_load("BMove",5.41,LVector3(0,0,15))
        self.setFrameRateMeter(True)
    
    def sm_load(self,mno,scno,ano):
        lono=loader.loadModel(mno)
        lono.setScale(scno)
        lono.flattenStrong()
        rig=lono.findAllMatches("**/+GeomNode")
        ga=rig.getPath(0).node().getGeom(0)
        shamesh=BulletTriangleMesh()
        shamesh.addGeom(ga)
        shape = BulletTriangleMeshShape(shamesh,dynamic=True)

        ri="Ri_{}".format(mno)
        self.rigig = self.worldNP.attachNewNode(BulletRigidBodyNode(ri))
        self.rigig.node().addShape(shape)
        self.rigig.setPos(ano)
        self.rigig.node().setMass(1)
        lono.reparentTo(self.rigig)

        self.world.attachRigidBody(self.rigig.node())

        return self.rigig

    def setup(self):
        self.worldNP = render.attachNewNode('World')


        self.debugNP = self.worldNP.attachNewNode(BulletDebugNode('Debug'))
        self.debugNP.show()


        self.debugNP.showTightBounds()
        self.debugNP.showBounds()

        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -12.0))
    
        self.world.setDebugNode(self.debugNP.node())    


    def update(self, task):
        dt = globalClock.getDt()
        self.world.doPhysics(dt, 5, 1.0/180.0)
        return task.cont
