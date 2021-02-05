from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random,time


while True:
    x,y,z = mc.player.getTilePos()
    x = x+1
    for j in range(10):
        color = random.randrange(0,16)
        z = z+1
        mc.setBlock(x,y-1,z,35,color)
        time.sleep(20)
        