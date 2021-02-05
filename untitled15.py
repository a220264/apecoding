from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getPos()


mc.setBlocks(x-10,y,z-10,x+10,y,z+10,22)
mc.setBlocks(x+10,y+20,z-10,x+10,y,z+10,22)
mc.setBlocks(x+10,y+20,z+10,x-10,y,z+10,22)
mc.setBlocks(x-10,y+20,z+10,x-10,y,z-10,22)
mc.setBlocks(x-10,y+20,z-10,x+10,y,z-10,22)
mc.setBlocks(x-9,y+1,z-9,x-8,y+1,z-8,169)
y-=1
while True:
   i=mc.getBlock(x,y,z)
   if i==169:
       mc.executeCommand('setworldspawn')
         