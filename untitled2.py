from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(50):
    x,y,z = mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,20)
mc.setBlocks(x-10,y-1,z-10,x+10,y+18,z+10,20)
