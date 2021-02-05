from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

A = randrange(0,16)
ID = mc.getPlayerEntityId("bobpig111")

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        date = block.data
        
        if date>A :
            mc.postToChat('E)$SU#SU')
        elif date<A:
            mc.postToChat('DL$!O')
        else:
            mc.setBlock(hit.pos,11)
            mc.postToChat('答對了')
        break
        
            