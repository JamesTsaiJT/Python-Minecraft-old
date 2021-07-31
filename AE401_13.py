# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:45:04 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from random import choice

mc = Minecraft.create()
#聊天機器人自動蓋房子
def building(x,y,z):
    try:
        name = input("請問客戶名稱?")
        length = int(input("請問房子長?"))
        weigth = int(input("請問房子寬?"))
        hight = int(input("請問房子高?"))
        material = int(input("請問房子建材?"))
        
        mc.setBlocks(x, y-1, z, x+length, y+hight, z+weigth, material)
        mc.setBlocks(x+1, y, z+1, x+length-1, y+hight-1, z+weigth-1, 0)
        mc.setBlocks(x+1, y, z+1, x+1, y+1, z, 0)
        
        mc.postToChat(name+"您的房子已蓋好")
    except:
        print("只能輸入數字")
        
        
#發牌機器人
def poker(x,y,z):
    player1_card = []
    player2_card = []
    cards_symbol = ["黑桃","紅心","紅磚","梅花"]
    cards_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    player1_status = input("請問玩家1狀態(ok or not ok):")
    if player1_status == "ok":
        print("ok")
        for i in range(3):
            card = [choice(cards_symbol)+choice(cards_number)]
            player1_card.append(card)
        mc.setSign(x,y,z,63,0,"player1's card",player1_card[0],player1_card[1],player1_card[2])
    
    elif player1_status == "not ok":
        print("get ready")
        return
    
    else:
        print("error")
        return
    
    
    player2_status = input("請問玩家2狀態(ok or not ok):")
    if player2_status == "ok":
        print("ok")
        for i in range(3):
            card = choice(cards_symbol)+choice(cards_number)
            player2_card.append(card)
        mc.setSign(x+3,y,z,63,0,"player2's card",player2_card[0],player2_card[1],player2_card[2])
    
    elif player2_status == "not ok":
        print("get ready")
        return
    
    else:
        print("error")
        return
    
    
        
        
x, y, z = mc.player.getTilePos()

#building(x,y,z)

poker(x,y,z)
    
    