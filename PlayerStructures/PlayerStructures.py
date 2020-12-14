from direct.showbase.ShowBase import ShowBase 
from panda3d.core import * 

class ShowApp(ShowBase): 

    def __init__(self): 
        ShowBase.__init__(self) 
        self.readbuff=open("InterBuff.py","r+")        
        self.taskMgr.add(self.interbuff,"InterBuff") 

    def interbuff(self,task): 
        exec(self.readbuff.read(),globals()) 
        self.readbuff.truncate(0) 
        self.readbuff.seek(0) 
        return task.cont 


def LoadingCharacter(DataCharacter):
    try:
        DataCharacter["model"].reparentTo(render)
    except Exception as modelexeception:
        print(modelexeception)
    
    try:
        DataCharacter["collisionData"]=CollisionNode("collisionData")
        DataCharacter["collisionCharacter"]=CollisionSphere(0,0,0,3)
        DataCharacter["collisionData"].addSolid(DataCharacter["collisionCharacter"])
        DataCharacter["collisionModel"]=DataCharacter["model"].attachNewNode(DataCharacter["collisionData"])
        DataCharacter["collisionModel"].show()
    except Exception as collisionexception:
        print(collisionexception)
        
    try:
        DataCharacter["texture"]=loader.loadTexture(DataCharacter["textureload"])
        DataCharacter["model"].setTexture(DataCharacter["texture"])
    except Exception as textureexception:
        print(textureexception)

AppBase=ShowApp()
charmodel=LoadingCharacter({"model":loader.loadModel("GemCell.egg"),"textureload":"Gretex.png"})                                                
AppBase.run() 