# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:36:35 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

#放置方塊機器人
blockType = int(input("請輸入要放的方塊ID："))
mc.setBlock(x, y, z, blockType)

"""
#進階放置方塊機器人
try:
    blockType = int(input("請輸入要放的方塊ID："))
    mc.setBlock(x, y, z, blockType)
except:
    print("只能輸入數字")
    #mc.postToChat("只能輸入數字")
"""
"""
#廣播發言
userName = input("請輸入姓名: ")
message = input("請輸入發言: ")
mc.postToChat(" ["+userName + "] " + message)
"""
