# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:02:52 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#a = input('你是誰?')
#postToChat('hello'+a+',今天天氣真好 我家門前有小河後面有山坡')
x,y,z = mc.player.getTilePos()

mc.setBlocks(x-10,y-1,z-10,x+10,y+18,z+10,87)
mc.setBlocks(x-9,y+1,z-9,x+9,y+17,z+9,0)
mc.setBlocks(x+10,y,z,x+10,y+3,z+1,0)
mc.setBlocks(x-10,y+9,z-10,x+10,y+10,z+10,87)