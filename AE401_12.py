# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:39:44 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from random import choice

mc = Minecraft.create()
"""
#用實體取得玩家座標位置，並從陣列中隨機取一個數並作為設置方塊的ID
mineral = [14,15,16,56,73,129]

r = choice(mineral)

myID = mc.getPlayerEntityId("xRinChika")
x,y,z = mc.entity.getTilePos(myID)

mc.setBlock(x,y,z,r)
"""
"""
#將二維陣列中的所有ID按照順序列印出來
list2d = [[12,41,14],
          [35,73,86]]

myID = mc.getPlayerEntityId("xRinChika")
x,y,z = mc.entity.getTilePos(myID)
startX = x

for list1d in list2d:#從第0行陣列開始，一次一行陣列
    for i in list1d:#從list1d陣列的第0個開始，一次一個數字
        mc.setBlock(x,y,z,i)
        
        x = x+1
    x = startX
    z = z+1
"""
"""
#字串擷取
string = "123456789 123456"
print(string.find("6"))
print(string.find("6",6))
print(string.find("6",6,15))
print(string[0:5])
"""

#擷取玩家的發言
print(str(mc.getPlayerEntityId("xRinChika")))
while True:
    chat = mc.events.pollChatPosts()
    #判斷是否有人發言，與點石成金用法相同
    if len(chat) > 0:
        mc.postToChat(chat[0])
        strChat = str(chat[0])
        length = len(strChat)
        print(strChat)
        print(length)
        
        #擷取出玩家的ID與說的話
        comma1 = strChat.find(",",0)
        comma2 = strChat.find(",",comma1+1)
        
        senderID = strChat[comma1+1:comma2]
        message = strChat[comma2+1+1:length-1]
        print(senderID)
        print(message)
        
        #反向用ID查出玩家的姓名
        playerName = mc.entity.getName(int(senderID))
        print(playerName)
    

