from panda3d.core import *
def run():

    sepand1=DirectionalLight("sela")

    mas=render.attachNewNode(sepand1)

    mas.setHpr(-18,-52,14)
    render.setLight(mas)
    
    sepand2=DirectionalLight("sela")

    mas=render.attachNewNode(sepand2)

    mas.setHpr(-18,-180,14)
    render.setLight(mas)
    
