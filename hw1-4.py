from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
Blocks = random.randrange(0,150)
x,y,z = mc.player.getTilePos()

mc.setBlocks(x-20,y-20,z-20,x+20,y+20,z+20,Blocks)
