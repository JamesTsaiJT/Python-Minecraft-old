# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:43:19 2021

@author: JamesTsai
"""

from mcpi.minecraft import Minecraft
from time import sleep
import random
mc = Minecraft.create()

def magic(x,y,z):
    for i in range(100):
        r = random.randrange(1,7)#控制方向
        d = random.randrange(1,5)#控制生成長度
        if r == 1:
            mc.setBlocks(x,y,z,x+d,y,z,48)
            x = x+d
        elif r == 2:
            mc.setBlocks(x,y,z,x-d,y,z,48)
            x = x-d
        elif r == 3:
            mc.setBlocks(x,y,z,x,y,z+d,48)
            z = z+d
        elif r == 4:
            mc.setBlocks(x,y,z,x,y,z-d,48)
            z = z-d
        elif r == 5:
            mc.setBlocks(x,y,z,x,y-d,z,48)
            y = y-d
        elif r == 6:
            mc.setBlocks(x,y,z,x,y+d,z,48)
            y = y+d
            
x, y, z = mc.player.getTilePos()
#magic(x,y,z)

while True:
    mc.executeCommand("weather clear")#"time add 50"
    sleep(0.05)
