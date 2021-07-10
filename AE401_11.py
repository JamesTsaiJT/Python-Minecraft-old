# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:22:16 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from random import randrange
from time import time,sleep

mc = Minecraft.create()
"""
#生成彩色地板躲貓貓
for i in range(10):
    x,y,z =mc.player.getTilePos()
    x = x+i
    
    for j in range(10):
        r = randrange(0,16)
        z = z+1
        mc.setBlock(x,y-1,z,35,r)
"""
"""
r = randrange(0,16)#先隨機獲得一個羊毛磚的Type，要猜這個是哪的方塊
while True:
    hits = mc.events.pollBlockHits()#取得敲擊到的方塊
    if len(hits)>0:
        hit = hits[0]#打敲擊到的方塊資料存到hit變數中
        
        block = mc.getBlockWithData(hit.pos)#用hit的方塊資料中的座標
        data = block.data#取得方塊的Type
        
        if data == r:#如果敲到的方塊Type就是random的值代表找到了
            mc.postToChat("you find it!")
            mc.setBlock(hit.pos,57)
            break
        elif data < r:
            mc.postToChat("too small, try to find another")
        elif data > r:
            mc.postToChat("too big, try to find another")
            
    sleep(0.3)
"""

#線性搜尋法
def LinerSearch():
    sTime = time()
    for i in range(100000001):
        if r == i:
            print("your computer find it, it's " + str(i))
            print("spend " + str(time()-sTime) + "sec")
            break
#二元搜尋法            
def BinarySearch():
    sTime = time()
    low = 0
    upper = 100000000
    
    while low <= upper:
        mid = (low+upper)//2
        
        if mid < r:
            low = mid+1
            
        elif mid > r:
            upper = mid-1
            
        else:
            print("your computer find it, it's " + str(mid))
            print("spend " + str(time()-sTime) + "sec")
            return


r = randrange(100000000)
LinerSearch()
#BinarySearch()

"""
myID = mc.getPlayerEntityId("xRinChika")
mc.postToChat(myID)

x,y,z = mc.entity.getTilePos(myID)
"""