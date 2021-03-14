# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:34:02 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
"""
t = 0

while True:
    t = t+1
    mc.postToChat("第"+str(t)+"次")
"""

x = -116
y = 67
z = -144
x = x+1
z = z+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x = x+1
z = z+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x = x+1
z = z+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)

"""
mc.postToChat("I'm watching you.")

while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("你現在位於X:"+str(x)+
                  "Y:"+str(y)+
                  "Z:"+str(z))
    time.sleep(0.5)
"""
