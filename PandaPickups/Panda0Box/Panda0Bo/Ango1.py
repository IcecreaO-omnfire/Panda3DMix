from direct.actor.Actor import Actor

class ango():
	def __init__(self):
		self.sano=Actor("EggMod/Sbig.egg",{"Anaib":"EggMod/Sbig-Armsjin.001.egg"})
		self.sano.reparentTo(render)
		self.sano.loop("Anaib")

runi=ango()