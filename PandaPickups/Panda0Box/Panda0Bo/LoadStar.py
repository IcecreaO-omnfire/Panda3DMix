from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import CollideMask
from panda3d.core import *
from panda3d.physics import *
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import random
import sys
import os
import math
import LoadStar


#Reload/Reparent to render
def loadRem(rem):
    relren=loader.loadModel(rem)
    relren.reparentTo(render)
    return relren
    
    
def davplay():
    cimo={"conp":NodePath("Sinse"),"col":CollisionNode("Manbe"),"ac":ActorNode("Sailes"),
    "menm":None,"frai":[sifpa],"dam":[],"clada":{}}
    return cimo
    
def sifpa(vpa):
    print(vpa["vpa"])
    
