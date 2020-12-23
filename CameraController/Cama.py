from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 

def camaPand(self,camMove):
    self["playerStore"]["parentCamera"].setY(self["playerStore"]["parentCamera"],camMove * 8 * globalClock.getDt())



class ShowApp(dict,ShowBase): 

    def __init__(self): 
        ShowBase.__init__(self) 
        self.disableMouse() 
        self.readbuff=open("InterBuff.py","r+")        
        self.taskMgr.add(self.interbuff,"InterBuff")
        self.accept('wheel_up', camaPand,extraArgs=[self,1])
        self.accept('wheel_down', camaPand,extraArgs=[self,-1]) 
        self["playerStore"]={"rotateCount":0,"heading":0,"pitch":0,"directionDirection":0,"rotate":0}
        self["playerStore"]["quatTo"]=Quat()
        self["playerStore"]["model"]=loader.loadModel("PenguiBall.egg")
        self["playerStore"]["model"].reparentTo(self.render)
        lookAt(self["playerStore"]["quatTo"],LPoint3f(40,10,0)-self["playerStore"]["model"].getPos(),Vec3.up())
        self["playerStore"]["parentCamera"]=render.attachNewNode("cameraSpace")

        #self["playerStore"]["parentCamera"].reparentTo(self["playerStore"]["model"])
        self["playerStore"]["parentCamera"].setEffect(CompassEffect.make(render))
        self.cam.reparentTo(self["playerStore"]["parentCamera"])
        self.cam.lookAt(self["playerStore"]["parentCamera"])
        #taskMgr.add(cameraSpot,"cameraAim")
        taskMgr.add(rotatePlacement, 'rotationFor',extraArgs=[self["playerStore"]],appendTask=True)          
        

    def interbuff(self,task): 
        exec(self.readbuff.read(),globals()) 
        self.readbuff.truncate(0) 
        self.readbuff.seek(0) 
        return task.cont 




def cameraSpot(task):
    if base.mouseWatcherNode.hasMouse():
        mouseX,mouseY=base.mouseWatcherNode.getMouse()
        #heading=base["playerStore"]["parentCamera"].getH()
        #pitch=base["playerStore"]["parentCamera"].getP()
        base.win.movePointer(0, int(base.win.getXSize()/2), int(base.win.getYSize()/2))        
        heading =-mouseX*10
        pitch =mouseY*10
        
        base["playerStore"]["parentCamera"].setHpr(base["playerStore"]["parentCamera"],heading,pitch,0)
        print(heading,pitch)
    return task.cont


def rotatePlacement(playerData,task):

    if playerData["rotateCount"]==10:
        if playerData["rotate"]==playerData["model"].getHpr():
            playerData["rotateCount"]=0
            return task.done
    elif playerData["rotate"]!=playerData["model"].getHpr():
        playerData["rotate"]=playerData["model"].getHpr()
        playerData["rotateCount"]=0
    playerData["rotateCount"]+=1

    quatProgress=playerData["quatTo"]


    
    playerData["directionDirection"]=0
    if quatProgress.getHpr()!=playerData["model"].getHpr():
        if quatProgress.getHpr()[0]!=playerData["model"].getH():
            playerData["directionDirection"]=(quatProgress.getHpr()[0]-playerData["model"].getH())
    if playerData["directionDirection"]>0:
        heading=min(quatProgress.getHpr()[0]-playerData["model"].getH(),8)
    elif playerData["directionDirection"]<=0:
        heading=min(playerData["model"].getH()-quatProgress.getHpr()[0],-8)
    if abs(quatProgress.getHpr()[0]-playerData["model"].getH())<1:
        return task.done
    print(playerData["model"].getHpr())
    print(quatProgress.getHpr())
    playerData["model"].setH(playerData["model"],heading)
    return task.cont
   
   

    
      
   
e=ShowApp()
e.run()