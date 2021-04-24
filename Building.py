# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:51:04 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

#蓋出空心的房子
width = 15
height = 10
length = 10
blockType = 4
light = 169
air = 0
mc.setBlocks(x, y, z, x+width, y+height, z+length, air)
#蓋房子
mc.setBlocks(x, y, z, x+width, y+height, z+length, blockType)
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, air)
#做門
mc.setBlocks(x+2, y, z, x+1, y+3, z, air)
#天花板的燈
mc.setBlocks(x, y+height, z, x+width, y+height, z+length, light)
#中間的燈
mc.setBlocks(x, y+height/2, z, x+width, y+height/2, z+length, light)
mc.setBlocks(x+2, y+height/2, z+2, x+width-2, y+height/2, z+length-2, air)