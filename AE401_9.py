# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:50:31 2021

@author: JamesTsai
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
    

def buildPyramid(x,y,z,base=10):
    height = (base//2)+1
    for i in range(height):
        x1 = x+i
        y1 = y+i
        z1 = z+i
        
        x2 = x+base-i
        z2 = z+base-i
        
        mc.setBlocks(x1,y1,z1,x2,y1,z2,24)
        
        
def nineNINE(x,y,z):
    line1 = []
    line2 = []
    line3 = []
    
    for i in range(1,4):
        line1.append(1*i)
    for i in range(1,4):
        line2.append(2*i)
    for i in range(1,4):
        line3.append(3*i)
        
    mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))
   
    
def virus(x,y,z,number):
    for i in range(8):
        for j in range(number):
            mc.spawnEntity(x,y,z,60)
            
        number = number*2
        
        mc.postToChat("這次生成了"+str(number)+"蠹魚")

        
x,y,z = x, y, z = mc.player.getTilePos()
#buildPyramid(x,y,z,100)
#nineNINE(x,y,z)
virus(x,y,z,3)
        