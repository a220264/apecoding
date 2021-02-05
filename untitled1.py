from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#a = input('你是誰?')
#postToChat('hello'+a+',今天天氣真好 我家門前有小河後面有山坡')
x,y,z = mc.player.getTilePos()

mc.setBlocks(x-10,y-1,z-10,x+10,y+18,z+10,87)
mc.setBlocks(x-9,y+1,z-9,x+9,y+17,z+9,0)
