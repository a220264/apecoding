from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos
number = 1

time.sleep(5)
for i in range(5):
    for i in range(number):
        mc.spawnEntity(x,y,z,101)
number*2