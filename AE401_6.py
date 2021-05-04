# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:40:54 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()

"""
#點石成金
gold_block_id = 41
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("恭喜你取得" + str(block))
        mc.setBlock(x,y,z,gold_block_id)
"""
"""
#告示牌
x, y, z = mc.player.getTilePos()        
mc.setSign(x,y,z,63,0,"程祐","老師","到此一遊","！！！")
"""
"""
#雞從天降
pos = mc.player.getPos()

while True:
    x = pos.x + random.uniform(-20,20)
    y = pos.y + 30
    z = pos.z + random.uniform(-20,20)
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.1)
"""

#爆破箭矢
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.createExplosion(x,y,z)