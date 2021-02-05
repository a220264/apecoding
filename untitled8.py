# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:39:05 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def planttree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,89)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
x,y,z, = mc.player.getPos()
for a in range(10):
    for b in range(10):
          planttree(x+b*a,y+b,z+a)