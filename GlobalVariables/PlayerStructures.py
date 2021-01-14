import GlobalPy
from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 

class ShowApp(ShowBase): 

    def __init__(self): 
        ShowBase.__init__(self) 


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
charmodel=LoadingCharacter({"model":loader.loadModel("box.egg"),GlobalPy.texa:"Gretex.png"})                                                
AppBase.run() 