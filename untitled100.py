# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:04:30 2020

@author: sami
"""

import random
answer=random.randint(1,10)
guess=input('1~10猜數字，猜錯我就罵你可憐哪')
guess=int(guess)
if guess<answer:
    print('可憐哪')
elif guess<answer:
    print('氣氣氣氣氣')
else:
    print('yee')
    
  

