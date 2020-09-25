from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import CollideMask
from panda3d.core import *
from panda3d.physics import *
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import *
from direct.actor.Actor import Actor
import random
import sys
import os
import math

class Pmango(PhysicsManager):
    def __init__(self):
        PhysicsManager.__init__(self)


class Moving(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # This is used to store which keys are currently pressed.
        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "back": 0, "up": 0}

        # Set up the environment
        #
        # This environment model contains collision meshes.  If you look
        # in the egg file, you will see the following:
        #
        #    <Collide> { Polyset keep descend }
        #
        # This tag causes the following mesh to be converted to a collision
        # mesh -- a mesh which is optimized for collision, not rendering.
        # It also keeps the original mesh, so there are now two copies ---
        # one optimized for rendering, one for collisions.

        self.environ = loader.loadModel("EggMod/SandPlan.egg")
        self.environ.reparentTo(render)
        self.environ.setScale(20)

        StartPos = LVector3(0,0,94)
        self.movint = loader.loadModel("EggMod/HailPar.egg")
        self.movint.reparentTo(render)
        self.movint.setScale(2)
        self.movint.setPos(StartPos + (0, 0, 0.5))


        # Accept the control keys for movement and rotation

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
        
        self.mopan=Pmango()
        
        self.alin = LinearEulerIntegrator()
        self.mopan.attachLinearIntegrator(self.alin)
        self.arin = AngularEulerIntegrator()
        self.mopan.attachAngularIntegrator(self.arin)
        
        taskMgr.doMethodLater(0.01,self.move, "moveTask")


        self.cTrav = CollisionTraverser()
        #base.cTrav.setRespectPrevTransform(True)
        

        self.actMove = NodePath("ActMove")
        self.actMove.reparentTo(render)
        self.an = ActorNode("BMova")
        self.anp = self.actMove.attachNewNode(self.an)
        

        
        self.mopan.attachPhysicalNode(self.an)
        self.movint.reparentTo(self.anp)

        self.anp.node().getPhysicsObject().setMass(1)
        #self.an.getPhysicsObject().setTerminalVelocity(1.0)

        self.dvi=0
        self.grava=ForceNode('GravAll')
        self.grar=render.attachNewNode(self.grava)
        self.grdi=LinearVectorForce(0.0,-0.0,-8.0)
        #self.grdi.setMassDependent(1)
        self.grava.addForce(self.grdi)  #Forces have to be added to force nodes and to
        # a physics manager
         
        self.mopan.addLinearForce(self.grdi)

        
        self.BMoveBalance = CollisionSphere(0, 0, -7.0, 1)
        self.BMoveBalanceNode = CollisionNode('BMove')
        self.BMoveBalanceNode.addSolid(self.BMoveBalance)
        

        self.BMoveBalancePath = self.movint.attachNewNode(self.BMoveBalanceNode)
        self.DinGro = PhysicsCollisionHandler()
        self.DinGro.setStaticFrictionCoef(1)
        self.DinGro.setDynamicFrictionCoef(2)
        self.DinGro.setAlmostStationarySpeed(0.1)

        self.DinGro.addCollider(self.BMoveBalancePath,self.anp) #Colliders use nodepaths for collisions instead of nodes
        self.cTrav.addCollider(self.BMoveBalancePath, self.DinGro)

        # Uncomment this line to see the collision rays
        self.BMoveBalancePath.show()

        # Uncomment this line to show a visual representation of the
        # collisions occuring
        self.cTrav.showCollisions(render)

        # Create some lighting
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((-5, -5, -5))
        render.setLight(render.attachNewNode(directionalLight))        


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
        #Wait(0.01)

        return task.again



