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

AppRead=ShowApp() 
AppRead.run() 
