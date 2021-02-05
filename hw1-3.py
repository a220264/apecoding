from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

While Ture:
    x,y,z = mc.player.getTilePos()
    mc.postToChat('你現在正在x :'+str(x)'y:'+str(y)'z:'+str(z))
    time.sleep(5)