from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.physics import *
from direct.task import *
import math

class loadModel():
    def __init__(self,obstart,mod1):
        obstart[mod1]=loader.loadModel(mod1)
        self.obstart=obstart[mod1]
        obstart[mod1].reparentTo(render)

        
        
        
class GRun(ShowBase,dict):
    def __init__(self):
        ShowBase.__init__(self)
        self.sound=loader.loadSfx("tone1.ogg")
        self.sound.setVolume(0.5)
        self.sound.setPlayRate(10)
        loadModel(self,"BuiltInBall1")
        self["BuiltInBall1"].setScale(0.5)
       # taskMgr.doMethodLater(0.01,self.projectile,"ProjectTraject")

        prsel(self,"BuiltInBall1")

        PandLight1=DirectionalLight("PandLight1")

        LightPath1=render.attachNewNode(PandLight1)

        LightPath1.setHpr(-18,-52,14)
        render.setLight(LightPath1)
    
        PandLight2=DirectionalLight("PandLight2")

        LightPath2=render.attachNewNode(PandLight2)

        LightPath2.setHpr(-18,-180,14)
        render.setLight(LightPath2)

    def projectile(self,task):
        a=-8.0
        b=20
        c=0.0
        points=(-b-math.sqrt(b**2-4*a*c)/(2*a),-b+math.sqrt(b**2-4*a*c)/(2*a))
        end=max(points)-min(points)
        XPlace=self["BuiltInBall1"].getX()
        if XPlace<4*end:
            z=(1/4)*a*(XPlace*1.0)**2+b*(XPlace*1.0)+c
            self["BuiltInBall1"].setPos(self["BuiltInBall1"].getX()+0.01,0,z)
            if self.sound.status()==AudioSound.READY:
                self.sound.play()
            arcdisplay=loader.loadModel("BuiltInBall1")
            arcdisplay.setPos(self["BuiltInBall1"].getPos())
            arcdisplay.setScale(0.5)
            arcdisplay.reparentTo(render)
            print(self["BuiltInBall1"].getPos())
            return task.again        

        
def prsel(self,access):
    print(self[access])
        

        
        
QuadRun=GRun()
QuadRun.run()
