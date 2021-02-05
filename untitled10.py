from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

import random
y=y-1
mc.setBlock(x,y,z,20)
for i in range(20):
    r = random.choice(range(1,7))
    if r==1:
        mc.setBlocks(x+1,y,z,x+3,y,z,20,)
        x=x+3
    if r==2:
        mc.setBlocks(x-1,y,z,x-3,y,z,20)
        x=x-3
    if r==3:
        mc.setBlocks(x,y,z+1,x,y,z+3,20)
        z=z+3
    if r==4:
        mc.setBlocks(x,y,z-1,x,y,z-3,20)
        z=z-3
    if r==5:
        mc.setBlocks(x,y+1,z,x,y+3,z,20)
        y=y+3
    if r==6:
        mc.setBlocks(x,y-1,z,x,y-3,z,20)
        y=y-3

