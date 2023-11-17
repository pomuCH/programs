#自作時計プログラム
import mcpi.minecraft as minecraft
import mcpi.block as block
import datetime
from drawing import *
import math
import time

d = Drawing()

dt_now = datetime.datetime.now()
hour=dt_now.hour
minute=dt_now.minute
second=dt_now.second
mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

x1=playerPos.x
y1=playerPos.y+19
z1=playerPos.z
i=0
a=0
r = 19
day=0
#####時計盤#####
for z in range(-r, r + 1):
  for x in range(-r, r + 1):
    if ((x**2 + z**2) <= r**2):
      mc.setBlock(
        playerPos.x + x,
        y1 + z,
        playerPos.z -3,
        block.STONE)
if hour>=12:
  hour-=12

if hour>=3:
  h_radian=360-(hour-3)*30
else:
  h_radian=90-(hour)*30
sin_h = round(math.sin(math.radians(h_radian)), 3)
cos_h = round(math.cos(math.radians(h_radian)), 3)
d.line(x1,y1,z1,x1+(10*cos_h),y1+(10*sin_h),z1,block.DIAMOND_BLOCK)

if minute>=15:
  d_radian=360-(minute-15)*6
  if minute>=30:
    h_radian-=15
else:
  d_radian=90-(minute)*6
sin_d = round(math.sin(math.radians(d_radian)), 3)
cos_d = round(math.cos(math.radians(d_radian)), 3)
d.line(x1,y1,z1-1,x1+(14*cos_d),y1+(14*sin_d),z1-1,block.GOLD_BLOCK)

if second>=15:
  s_radian=360-(second-15)*6
else:
  s_radian=90-(second)*6
sin_s = round(math.sin(math.radians(s_radian)), 3)
cos_s = round(math.cos(math.radians(s_radian)), 3)
d.line(x1,y1,z1-2,x1+(17*cos_s),y1+(17*sin_s),z1-2,block.IRON_BLOCK)#2点間に線を引く

while True:
  s_radian-=6
  for x in range(0, 38):
    for i in range(0,38):
      mc.setBlock(playerPos.x - 19 + i, playerPos.y + x, playerPos.z-2, block.AIR)
  sin_s = round(math.sin(math.radians(s_radian)), 3)
  cos_s = round(math.cos(math.radians(s_radian)), 3)
  if s_radian==0:
    s_radian+=360
  elif s_radian==90:
    d_radian-=6
    for x in range(0, 38):
      for i in range(0,38):
        mc.setBlock(playerPos.x - 19 + i, playerPos.y + x, playerPos.z-1, block.AIR)
    sin_d = round(math.sin(math.radians(d_radian)), 3)
    cos_d = round(math.cos(math.radians(d_radian)), 3)
    if d_radian==0:
      d_radian+=360
    elif d_radian==90 or d_radian==270:
      h_radian-=15
      for x in range(0, 38):
        for i in range(0,38):
          mc.setBlock(playerPos.x - 19 + i, playerPos.y + x, playerPos.z, block.AIR)
      sin_h = round(math.sin(math.radians(h_radian)), 3)
      cos_h = round(math.cos(math.radians(h_radian)), 3)
      if h_radian==0:
        h_radian+=360
  d.line(x1,y1,z1-2,x1+(17*cos_s),y1+(17*sin_s),z1-2,block.IRON_BLOCK)
  d.line(x1,y1,z1-1,x1+(14*cos_d),y1+(14*sin_d),z1-1,block.GOLD_BLOCK)
  d.line(x1,y1,z1,x1+(10*cos_h),y1+(10*sin_h),z1,block.DIAMOND_BLOCK)
  time.sleep(1)
  if i==100000:
    break



#mc.postToChat("apapapa")
