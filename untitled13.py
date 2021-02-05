#標題:正版的Minecraft 盜版的漆彈
#程式:
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    i = mc.events.pollProjectileHits()
    if len(i)>0:
        j = i[0]
        x,y,z = j.pos.x,j.pos.y,j.pos.z
        mc.setBlock(x,y-1,z,87)
