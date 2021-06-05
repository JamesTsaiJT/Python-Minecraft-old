# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:05:07 2021

@author: JamesTsai
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    leaves = 18
    trunk = 17
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,leaves)
    mc.setBlocks(x,y,z,x,y+4,z,trunk)
    
def giant(x,y,z):
    iron = 42
    pumpkin = 86
    air = 0
    mc.setBlock(x,y,z,iron)
    mc.setBlocks(x-1,y+1,z,x+1,y+1,z,iron)
    mc.setBlock(x,y+2,z,pumpkin)
    mc.setBlock(x-1,y,z,air)
    mc.setBlock(x+1,y,z,air)
    
def bomber(x,y,z):
    TNT = 46
    mc.setBlock(x,y,z,TNT)

x, y, z = mc.player.getTilePos()

#蓋一棵樹
#plantTree(x,y,z)
#giant(x,y,z)
"""
#蓋一排樹
for i in range(0,50,5):
    #plantTree(x+i,y,z)
    giant(x,y,z)
"""
"""
#蓋一片森林
for i in range(0,30,3):
    for j in range(0,30,3):
        plantTree(x+i,y,z+j)
"""

#一隻鐵人
#giant(x,y,z)
"""
#一排鐵人
for i in range(0,50,5):
    giant(x+i,y,z)
"""
"""
#鐵人軍團
for i in range(0,30,3):
    for j in range(0,30,3):
        giant(x+i,y,z+j)
"""

"""
#地爆天星
for i in range(0,30,3):
    for j in range(0,30,3):
        for k in range(0,30,3):
            bomber(x+i,y+j,z+k)
"""
while True:
    x, y, z = mc.player.getTilePos()
    blockData = mc.getBlockWithData(x,y-1,z)
    data = blockData.data
    if data==15:
        mc.postToChat("前面是死路")
        
    

#/summon giant