
#from pandac.PandaModules import loadPrcFileData
#loadPrcFileData('', 'load-display pandagl')

#loadPrcFileData('', 'bullet-additional-damping true')
#loadPrcFileData('', 'bullet-additional-damping-linear-factor 0.005')
#loadPrcFileData('', 'bullet-additional-damping-angular-factor 0.01')
#loadPrcFileData('', 'bullet-additional-damping-linear-threshold 0.01')
#loadPrcFileData('', 'bullet-additional-damping-angular-threshold 0.01')
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'window-title Occluder Demo')
loadPrcFileData('', 'sync-video false')
loadPrcFileData('', 'show-frame-rate-meter true')
loadPrcFileData('', 'texture-minfilter linear-mipmap-linear')


import sys
#import direct.directbase.DirectStart

from direct.showbase.DirectObject import DirectObject
from direct.directtools.DirectCameraControl import *
from direct.showbase.InputStateGlobal import inputState
from direct.showbase.ShowBase import *

from panda3d.core import *

from panda3d.bullet import *




class Game(ShowBase):

  def __init__(self):
  
    ShowBase.__init__(self)
    #DirectCameraControl.enableMouseFly(self)
    base.setBackgroundColor(0.1, 0.1, 0.8, 1)
    self.setFrameRateMeter(True)
    render.setTwoSided(True)
    base.disableMouse()
    #base.cam.setPos(0, 20, 4)
    #base.cam.lookAt(0, 0, 0)



    # Input
    self.accept('escape', self.doExit)
    self.accept('r', self.doReset)
    inputState.watchWithModifiers('forward', 'w')
    inputState.watchWithModifiers('left', 'a')
    inputState.watchWithModifiers('reverse', 's')
    inputState.watchWithModifiers('right', 'd')
    inputState.watchWithModifiers('turnLeft', 'q')
    inputState.watchWithModifiers('turnRight', 'e')
    inputState.watchWithModifiers('space', 'f')

    # Task
    taskMgr.add(self.update, 'updateWorld')

    # Physics
    self.setup()

  # _____HANDLER_____

  def doExit(self):
    self.cleanup()
    sys.exit(1)

  def doReset(self):
    self.cleanup()
    self.setup()



  # ____TASK___



  def update(self, task):
    dt = globalClock.getDt()

    #self.processInput(dt)
    #self.world.doPhysics(dt)
    self.world.doPhysics(dt, 5, 1.0/180.0)

    return task.cont

  def cleanup(self):
    self.world.removeRigidBody(self.groundNP.node())
    self.world.removeRigidBody(self.boxNP.node())
    self.world = None

    self.debugNP = None
    self.groundNP = None
    self.boxNP = None

    self.worldNP.removeNode()

  def setup(self):
    self.worldNP = render.attachNewNode('World')

    # World
    self.debugNP = self.worldNP.attachNewNode(BulletDebugNode('Debug'))
    self.debugNP.show()
    #self.debugNP.node().showWireframe(True)
    #self.debugNP.node().showConstraints(True)
    #self.debugNP.node().showBoundingBoxes(True)
    #self.debugNP.node().showNormals(True)

    self.debugNP.showTightBounds()
    self.debugNP.showBounds()

    self.world = BulletWorld()
    self.world.setGravity(Vec3(0, 0, -12.0))
    
    self.world.setDebugNode(self.debugNP.node())

    #StaticLoading
    def sm_load(mno,scno,ano):
        lono=loader.loadModel(mno)
        lono.setScale(scno)
        lono.flattenStrong()
        rig=lono.findAllMatches("**/+GeomNode")
        ga=rig.getPath(0).node().getGeom(0)
        shamesh=BulletTriangleMesh()
        shamesh.addGeom(ga)
        shape = BulletTriangleMeshShape(shamesh,dynamic=False)
        
        ri="Ri_{}".format(mno)
        self.rigig = self.worldNP.attachNewNode(BulletRigidBodyNode(ri))
        self.rigig.node().addShape(shape)
        self.rigig.setPos(ano)
        self.rigig.node()
        lono.reparentTo(self.rigig)

        self.world.attachRigidBody(self.rigig.node())

    #DynamicLoading
    def dm_load(mno,scno,ano):
        lono=loader.loadModel(mno)
        lono.setScale(scno)
        lono.flattenStrong()
        rig=lono.findAllMatches("**/+GeomNode")
        ga=rig.getPath(0).node().getGeom(0)
        shamesh=BulletTriangleMesh()
        shamesh.addGeom(ga)
        shape = BulletTriangleMeshShape(shamesh,dynamic=True)
        
        ri="Ri_{}".format(mno)
        self.ri = self.worldNP.attachNewNode(BulletRigidBodyNode(ri))
        self.ri.node().addShape(shape)
        self.ri.setPos(ano)
        self.ri.node().setMass(1.0)
        lono.reparentTo(self.ri)
        self.cam.reparentTo(self.ri)
        self.cam.setPos(LVector3(-140,0,0))
        self.cam.lookAt(self.ri)
        self.world.attachRigidBody(self.ri.node())

        
    sm_load("SandPlan",47,LVector3(0,0,0))
    dm_load("BMove",6.5,LVector3(0,0,161))
    sepand1=DirectionalLight("sela")

    mas=render.attachNewNode(sepand1)

    mas.setHpr(-18,-52,14)
    render.setLight(mas)




    # Bullet nodes should survive a flatten operation!
    #self.worldNP.flattenStrong()
    #render.ls()

game = Game()


run()




