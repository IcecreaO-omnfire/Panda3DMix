#!/usr/bin/env python

from panda3d.core import *
# Tell Panda3D to use OpenAL, not FMOD
loadPrcFileData("", "audio-library-name p3openal_audio")

from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase



class Video():
    def __init__(self,media):
        self.tex = MovieTexture("Crypt")
        self.sound = loader.loadSfx(media)
        self.success = self.tex.read(media)
        self.cm = CardMaker("Card Crypt") 
        self.card = NodePath(self.cm.generate()) 
        self.card.reparentTo(render)
        self.card.setTexture(self.tex)

  

class VOn():
    def __init__(self,mediastart):
        self.mediastart=mediastart

    def play(self):
        self.mediastart.tex.play()
        self.mediastart.sound.play()

class VOff2():
    def __init__(self,mediastart):
        self.mediastart=mediastart

    def stop(self):
        self.mediastart.tex.pause()
        self.mediastart.sound.pause()
    

class MediaPlayer(ShowBase):

    def __init__(self, media_file):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)
        self.runmedia=0


        # Load the texture. We could use loader.loadTexture for this,
        # but we want to make sure we get a MovieTexture, since it
        # implements synchronizeTo.
        vim=Video("Crt.mkv")
        pon=VOn(vim)
        poff=VOff2(vim)
        #pon.play()

        self.accept("enter",self.BRun,extraArgs=[pon,poff])

        # Set up a fullscreen card to set the video texture on.
        
        #cm.setFrameFullscreenQuad()

        # Tell the CardMaker to create texture coordinates that take into
        # account the padding region of the texture.
        #cm.setUvRange(self.tex)

        # Now place the card in the scene graph and apply the texture to it.


        # Synchronize the video to the sound.
        #self.tex.synchronizeTo(self.sound)

        #self.sound.play()
        #self.tex.play()
    def BRun(self,pvideo,poff):
        if self.runmedia==0: 
            pvideo.play()
            self.runmedia+=1
        elif self.runmedia==1:
            poff.stop()
            self.runmedia-=1

player = MediaPlayer("Crt.avi")
player.run()
