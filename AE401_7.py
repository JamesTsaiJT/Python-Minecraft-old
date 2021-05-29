# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:39:34 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

for i in range(20):
    #蓋直的路
    mc.setBlock(x,y-1,z+i)
    #蓋斜的路
    #mc.setBlock(x+i,y-1,z+i)