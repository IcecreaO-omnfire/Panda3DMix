#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.4 on Wed Oct 16 20:56:29 2019
#

import wx
import wx.grid
try:
    from coconut.convenience import parse
except:
    pass
import sys
from panda3d.core import LVector3
from panda3d.core import *
import time
import magipanda

nrun=0
vino="Prompt GoInitialize"
spout=open("Panddaout.txt","a+")
mopspeed=1
vis=time.clock()

class Int2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Int2.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.B02 = wx.Button(self, wx.ID_ANY, "Load Input")
        self.B03 = wx.Button(self, wx.ID_ANY, "Run")
        self.B01 = wx.Button(self, wx.ID_ANY, "Reload Main")
        self.B04 = wx.Button(self, wx.ID_ANY, "Scene Nodes Hierarchy")
        self.B_05 = wx.Button(self, wx.ID_ANY, "Set Mation")
        self.B05 = wx.Button(self, wx.ID_ANY, "Select Node 1")
        self.B06 = wx.Button(self, wx.ID_ANY, "Select Node 2")
        self.B07 = wx.Button(self, wx.ID_ANY, "Select Node 3")
        self.B08 = wx.Button(self, wx.ID_ANY, "Select Node 4")
        self.Seltin_01 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB | wx.TE_READONLY)
        self.Seltin_02 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB | wx.TE_READONLY)
        self.Seltin_03 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB | wx.TE_READONLY)
        self.Seltin_04 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB | wx.TE_READONLY)
        self.B_18 = wx.Button(self, wx.ID_ANY, "Select Node")
        self.B_37 = wx.Button(self, wx.ID_ANY, "S+")
        self.B_19 = wx.Button(self, wx.ID_ANY, "Get Children")
        self.B_25 = wx.Button(self, wx.ID_ANY, "U")
        self.B_38 = wx.Button(self, wx.ID_ANY, "S-")
        self.B_20 = wx.Button(self, wx.ID_ANY, "Get Paths")
        self.B_27 = wx.Button(self, wx.ID_ANY, "L")
        self.B_28 = wx.Button(self, wx.ID_ANY, "R")
        self.B_21 = wx.Button(self, wx.ID_ANY, "Rotate")
        self.B_26 = wx.Button(self, wx.ID_ANY, "D")
        self.B_29 = wx.Button(self, wx.ID_ANY, "F")
        self.B_22 = wx.Button(self, wx.ID_ANY, "Move")
        self.B_36 = wx.Button(self, wx.ID_ANY, "B")
        self.Tein1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        self.B_33 = wx.Button(self, wx.ID_ANY, "RMW\nRM1")
        self.B_30 = wx.Button(self, wx.ID_ANY, "Restart Interpreter")
        self.B_31 = wx.Button(self, wx.ID_ANY, "Enter")
        self.Racinp1 = wx.RadioButton(self, wx.ID_ANY, "Main Interpreter", style=wx.RB_GROUP)
        self.Racinp2 = wx.RadioButton(self, wx.ID_ANY, "Coconut Interpreter")
        self.Teout1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB | wx.TE_READONLY)
        self.B_32 = wx.Button(self, wx.ID_ANY, "RFW")
        self.B_34 = wx.Button(self, wx.ID_ANY, "RFW")
        self.B_35 = wx.Button(self, wx.ID_ANY, "RFW")
        self.B13 = wx.Button(self, wx.ID_ANY, "Load Model")
        self.B14 = wx.Button(self, wx.ID_ANY, "Add Node")
        self.B15 = wx.Button(self, wx.ID_ANY, "Remove Node")
        self.B16 = wx.Button(self, wx.ID_ANY, "Instance To")

        self.__set_properties()
        self.__do_layout()
        sys.stdout=self
        sys.stderr=self
        sys.stdin=self

        self.Bind(wx.EVT_BUTTON, self.fpanin, self.B02)
        self.Bind(wx.EVT_BUTTON, self.runmain, self.B03)
        self.Bind(wx.EVT_BUTTON, self.remain, self.B01)
        self.Bind(wx.EVT_BUTTON, self.npandhi, self.B04)
        self.Bind(wx.EVT_BUTTON, self.inreback, self.B_05)
        self.Bind(wx.EVT_BUTTON, self.satin1, self.B05)
        self.Bind(wx.EVT_BUTTON, self.satin2, self.B06)
        self.Bind(wx.EVT_BUTTON, self.satin3, self.B07)
        self.Bind(wx.EVT_BUTTON, self.satin4, self.B08)
        self.Bind(wx.EVT_BUTTON, self.sele_1, self.B_18)
        self.Bind(wx.EVT_BUTTON, self.spand1, self.B_37)
        self.Bind(wx.EVT_BUTTON, self.chi_1, self.B_19)
        self.Bind(wx.EVT_BUTTON, self.upan1, self.B_25)
        self.Bind(wx.EVT_BUTTON, self.spand2, self.B_38)
        self.Bind(wx.EVT_BUTTON, self.path_1, self.B_20)
        self.Bind(wx.EVT_BUTTON, self.lepan1, self.B_27)
        self.Bind(wx.EVT_BUTTON, self.ripan1, self.B_28)
        self.Bind(wx.EVT_BUTTON, self.mprotate, self.B_21)
        self.Bind(wx.EVT_BUTTON, self.dopan1, self.B_26)
        self.Bind(wx.EVT_BUTTON, self.fopand1, self.B_29)
        self.Bind(wx.EVT_BUTTON, self.mpmove, self.B_22)
        self.Bind(wx.EVT_BUTTON, self.bapand1, self.B_36)
        self.Bind(wx.EVT_BUTTON, self.interback, self.B_30)
        self.Bind(wx.EVT_BUTTON, self.teinen, self.B_31)
        self.Bind(wx.EVT_RADIOBUTTON, self.MaiIn, self.Racinp1)
        self.Bind(wx.EVT_RADIOBUTTON, self.ConIn, self.Racinp2)
        self.Bind(wx.EVT_BUTTON, self.clteout, self.B_35)
        self.Bind(wx.EVT_BUTTON, self.pmod1, self.B13)
        self.Bind(wx.EVT_BUTTON, self.padd1, self.B14)
        self.Bind(wx.EVT_BUTTON, self.prem1, self.B15)
        self.Bind(wx.EVT_BUTTON, self.pandinsel, self.B16)
        # end wxGlade
    
    def write(self,iney):
        global vino
        vino+=iney
        self.Teout1.ScrollLines(-1)
        self.Teout1.AppendText("##########")
        self.Teout1.AppendText(iney)
        self.Teout1.AppendText("----------")

    def __set_properties(self):
        # begin wxGlade: Int2.__set_properties
        self.SetTitle("Panda0Box")
        self.SetBackgroundColour(wx.Colour(50, 153, 204))
        self.Seltin_01.SetBackgroundColour(wx.Colour(143, 143, 188))
        self.Seltin_02.SetBackgroundColour(wx.Colour(143, 143, 188))
        self.Seltin_03.SetBackgroundColour(wx.Colour(143, 143, 188))
        self.Seltin_04.SetBackgroundColour(wx.Colour(143, 143, 188))
        self.B_37.SetMinSize((28, 26))
        self.B_25.SetMinSize((28, 26))
        self.B_38.SetMinSize((28, 26))
        self.B_27.SetMinSize((28, 26))
        self.B_28.SetMinSize((28, 26))
        self.B_26.SetMinSize((28, 26))
        self.B_29.SetMinSize((28, 26))
        self.B_36.SetMinSize((28, 26))
        self.Tein1.SetMinSize((200, 400))
        self.Tein1.SetBackgroundColour(wx.Colour(0, 165, 188))
        self.B_33.Hide()
        self.B_30.Hide()
        self.Teout1.SetMinSize((200, 400))
        self.Teout1.SetBackgroundColour(wx.Colour(143, 143, 188))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Int2.__do_layout
        Spota = wx.GridBagSizer(0, 0)
        Bsp4 = wx.GridBagSizer(0, 0)
        Bsp8 = wx.GridBagSizer(0, 0)
        Bsp5_copy_1 = wx.GridBagSizer(0, 0)
        Bsp6 = wx.GridBagSizer(0, 0)
        Bsp7 = wx.GridBagSizer(0, 0)
        Bsp3 = wx.GridBagSizer(0, 0)
        Bsp5 = wx.GridBagSizer(0, 0)
        Bsp2 = wx.GridBagSizer(0, 0)
        Bsp1 = wx.GridBagSizer(0, 0)
        Bsp1.Add(self.B02, (0, 0), (1, 1), 0, 0)
        Bsp1.Add(self.B03, (0, 1), (1, 1), 0, 0)
        Bsp1.Add(self.B01, (0, 2), (1, 1), 0, 0)
        Spota.Add(Bsp1, (0, 0), (1, 1), wx.EXPAND, 0)
        Spota.Add(self.B04, (0, 1), (1, 1), 0, 0)
        #Spota.Add(self.B_05, (0, 2), (1, 1), 0, 0)
        Bsp2.Add(self.B05, (0, 0), (1, 1), 0, 0)
        Bsp2.Add(self.B06, (0, 1), (1, 1), 0, 0)
        Bsp2.Add(self.B07, (0, 2), (1, 1), 0, 0)
        Bsp2.Add(self.B08, (0, 3), (1, 1), 0, 0)
        Bsp2.Add(self.Seltin_01, (1, 0), (1, 1), wx.ALL, 0)
        Bsp2.Add(self.Seltin_02, (1, 1), (1, 1), wx.ALL, 0)
        Bsp2.Add(self.Seltin_03, (1, 2), (1, 1), wx.ALL, 0)
        Bsp2.Add(self.Seltin_04, (1, 3), (1, 1), wx.ALL, 0)
        Spota.Add(Bsp2, (1, 0), (1, 1), wx.EXPAND, 0)
        Bsp3.Add(132, 400, (0, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_18, (0, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_37, (0, 5), (1, 1), 0, 0)
        Bsp5.Add(self.B_19, (1, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_25, (1, 3), (1, 1), 0, 0)
        Bsp5.Add(self.B_38, (1, 5), (1, 1), 0, 0)
        Bsp5.Add(self.B_20, (2, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_27, (2, 2), (1, 1), 0, 0)
        Bsp5.Add(self.B_28, (2, 4), (1, 1), 0, 0)
        Bsp5.Add(self.B_21, (3, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_26, (3, 3), (1, 1), 0, 0)
        Bsp5.Add(self.B_29, (3, 5), (1, 1), 0, 0)
        Bsp5.Add(self.B_22, (4, 0), (1, 1), 0, 0)
        Bsp5.Add(self.B_36, (4, 5), (1, 1), 0, 0)
        Bsp3.Add(Bsp5, (0, 1), (1, 1), wx.EXPAND, 0)
        Spota.Add(Bsp3, (2, 0), (1, 1), wx.EXPAND, 0)
        Bsp6.Add(self.Tein1, (0, 0), (1, 1), wx.ALL, 0)
        Bsp7.Add(self.B_33, (0, 0), (1, 1), 0, 0)
        Bsp7.Add(self.B_30, (1, 0), (1, 1), 0, 0)
        Bsp7.Add(self.B_31, (2, 0), (1, 1), 0, 0)
        Bsp7.Add(self.Racinp1, (3, 0), (1, 1), 0, 0)
        Bsp7.Add(self.Racinp2, (4, 0), (1, 1), 0, 0)
        Bsp6.Add(Bsp7, (0, 1), (1, 1), wx.EXPAND, 0)
        Spota.Add(Bsp6, (2, 1), (1, 1), wx.EXPAND, 0)
        Bsp8.Add(self.Teout1, (0, 0), (1, 1), wx.ALL, 0)
        #Bsp5_copy_1.Add(self.B_32, (0, 0), (1, 1), 0, 0)
        #Bsp5_copy_1.Add(self.B_34, (1, 0), (1, 1), 0, 0)
        #Bsp5_copy_1.Add(self.B_35, (2, 0), (1, 1), 0, 0)
        Bsp8.Add(Bsp5_copy_1, (0, 1), (1, 1), wx.EXPAND, 0)
        Spota.Add(Bsp8, (2, 2), (1, 1), wx.EXPAND, 0)
        Bsp4.Add(self.B13, (0, 0), (1, 1), 0, 0)
        Bsp4.Add(self.B14, (0, 1), (1, 1), 0, 0)
        Bsp4.Add(self.B15, (0, 2), (1, 1), 0, 0)
        Bsp4.Add(self.B16, (0, 3), (1, 1), 0, 0)
        Spota.Add(Bsp4, (3, 0), (1, 1), wx.EXPAND, 0)
        self.SetSizer(Spota)
        Spota.Fit(self)
        self.Layout()
        # end wxGlade

    def fpanin(self, event):  # wxGlade: Int2.<event_handler>
        spin=open("Panddatin.txt","r+")
        Panda0Box.F1.Tein1.AppendText(spin.read())

    def runmain(self, event):  # wxGlade: Int2.<event_handler>
        global nrun
        if nrun==0:
            nrun=1
            runthe()
        if nrun>=1:
            nrun=0

    def remain(self, event):  # wxGlade: Int2.<event_handler>
        import importlib
        importlib.reload(magipanda)

    def npandhi(self, event):  # wxGlade: Int2.<event_handler>
        hierapio=F2(None,wx.ID_ANY,"")
        hierapio.Show()
        tipe=hierapio.Btin.AddRoot("Render",data=Panda0Box.pamo.render)
        oftre(hierapio,tipe,Panda0Box.pamo.render)

    def inreback(self, event):  # wxGlade: Int2.<event_handler>
        print("Event handler 'inreback' not implemented!")
        event.Skip()

    def satin1(self, event):  # wxGlade: Int2.<event_handler>
        global sepand1
        global sano1
        sano1=sepand1
        Panda0Box.F1.Seltin_01.Value=sano1.getName()

    def satin2(self, event):  # wxGlade: Int2.<event_handler>
        global sepand2
        global sano2
        sano2=sepand2
        Panda0Box.F1.Seltin_02.Value=sano2.getName()

    def satin3(self, event):  # wxGlade: Int2.<event_handler>
        global sepand3
        global sano3
        sano3=sepand3
        Panda0Box.F1.Seltin_03.Value=sano3.getName()
    def satin4(self, event):  # wxGlade: Int2.<event_handler>
        global sepand4
        global sano4
        sano4=sepand4
        Panda0Box.F1.Seltin_04.Value=sano4.getName()

    def sele_1(self, event):  # wxGlade: Int2.<event_handler>
        Panda0Box.F1.Tein1.AppendText("sano=")

    def spand1(self, event):  # wxGlade: Int2.<event_handler>
        global mopspeed
        mopspeed+=1

    def chi_1(self, event):  # wxGlade: Int2.<event_handler>
        global sano
        print(sano.getChildren())

    def upan1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(0,1*mopspeed,0))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(0,1*mopspeed,0))

    def spand2(self, event):  # wxGlade: Int2.<event_handler>
        global mopspeed
        mopspeed-=1

    def path_1(self, event):  # wxGlade: Int2.<event_handler>
        global sano
        print(sano.getPaths())

    def lepan1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(0,0,-1*mopspeed))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(0,0,-1*mopspeed))

    def ripan1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(0,0,1*mopspeed))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(0,0,1*mopspeed))

    def mprotate(self, event):  # wxGlade: Int2.<event_handler>
        global samode
        samode=1

    def dopan1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(0,-1*mopspeed,0))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(0,-1*mopspeed,0))

    def fopand1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(1*mopspeed,0,0))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(1*mopspeed,0,0))    

    def mpmove(self, event):  # wxGlade: Int2.<event_handler>
        global samode
        samode=0

    def bapand1(self, event):  # wxGlade: Int2.<event_handler>
        if samode==0:
            sano.setPos(sano.getPos()+LVector3(-1*mopspeed,0,0))
        if samode==1:
            sano.setHpr(sano.getHpr()+LVector3(-1*mopspeed,0,0))   

    def interback(self, event):  # wxGlade: Int2.<event_handler>
        print("Event handler 'interback' not implemented!")
        event.Skip()

    def teinen(self, event):  # wxGlade: Int2.<event_handler>
        spout.write("\n")
        spout.write(Panda0Box.F1.Tein1.Value)
        spout.write("\n")
        spout.flush()
        tefie()

    def MaiIn(self, event):  # wxGlade: Int2.<event_handler>
        event.Skip()

    def ConIn(self, event):  # wxGlade: Int2.<event_handler>
        event.Skip()

    def clteout(self, event):  # wxGlade: Int2.<event_handler>
        print("Event handler 'clteout' not implemented!")
        event.Skip()

    def pmod1(self, event):  # wxGlade: Int2.<event_handler>
        global sano
        Panda0Box.F1.Tein1.AppendText("loader.loadModel(")       

    def padd1(self, event):  # wxGlade: Int2.<event_handler>
        Panda0Box.F1.Tein1.AppendText("render.attachNewNode(")  

    def prem1(self, event):  # wxGlade: Int2.<event_handler>
        global sano
        Panda0Box.F1.Tein1.AppendText("sano"+".removeNode()")

    def pandinsel(self, event):  # wxGlade: Int2.<event_handler>
        Panda0Box.F1.Tein1.AppendText("npai=render.attachNewNode(")
        Panda0Box.F1.Tein1.AppendText("\n")
        Panda0Box.F1.Tein1.AppendText("sano.instanceTo(npai)")

# end of class Int2

class F2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: F2.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.Btin = wx.TreeCtrl(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.apontree1, self.Btin)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: F2.__set_properties
        self.SetTitle("Selected Hierarchy")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: F2.__do_layout
        SPBin1 = wx.BoxSizer(wx.VERTICAL)
        SPBin1.Add(self.Btin, 1, wx.EXPAND, 0)
        self.SetSizer(SPBin1)
        self.Layout()
        # end wxGlade

    def apontree1(self, event):  # wxGlade: F2.<event_handler>
        global sano
        sano=self.Btin.GetItemData(self.Btin.GetFocusedItem())
        print(sano)
# end of class F2

def runthe():
    global nrun
    while nrun==1:
        Panda0Box.pamo.taskMgr.step()
        time.sleep(0.01)

def tefie():
    if Panda0Box.F1.Racinp2.Value==True:
        exec(parse(Panda0Box.F1.Tein1.Value),globals())
        print("Coconut Executed:"+"\n"+Panda0Box.F1.Tein1.Value)
    if Panda0Box.F1.Racinp1.Value==True:
        exec((Panda0Box.F1.Tein1.Value),globals())
    

class IntRun(wx.App):
    def OnInit(self):
        self.F1=Int2(None,wx.ID_ANY,"")
        self.SetTopWindow(self.F1)
        #self.pamo=magipanda.Magip()
        self.F1.Show()
        self.F1.Teout1.AppendText(vino)
        return True

class oftre():
    def __init__(self,hier,pasnop,pasno):
        self.pasnin=hier.Btin.AppendItem(pasnop,pasno.getName(),data=pasno)
        self.pasni=pasno
        try:
            for arn in self.pasni.getChildren():
                oftre(hier,self.pasnin,arn)
        except:
            pass
    
    def nad(self):
        return self.pasnin




Panda0Box = IntRun(0)
vis=time.clock()-vis
print(vis)
Panda0Box.MainLoop()