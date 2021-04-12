# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:36:04 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
"""
#蓋出空心的房子
width = 10
height = 5
length = 6
blockType = 4
air = 0
mc.setBlocks(x, y, z, x+width, y+height, z+length, blockType)
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, air)
"""
"""
#輕功水上漂
a = mc.getBlock(x, y-1, z+1)
b = mc.getBlock(x, y-1, z-1)
c = mc.getBlock(x+1, y-1, z)
d = mc.getBlock(x+1, y-1, z)
if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
    mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 103)
"""
"""
花花世界
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, 38)
    time.sleep(0.2)
"""
"""
#海綿水壩
a = 0
while a<20:
    mc.setBlocks(x+30, y-1, z, x-30, y-10, z, 19)
    z=z-5
    a=a+1
"""

#詛咒
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x,y,z,8)
    time.sleep(3)
