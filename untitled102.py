# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:23:28 2020

@author: sami
"""

import random
answer=random.randint(1,50)
a=  1
b=50
c=0
while c <5:
    guess=input(str(a)+'~'+str(b)+'猜數字，猜錯我就罵你可憐哪')
    guess=int(guess)
    
    if guess<answer:
        print('可憐哪')
        a=guess
        c+=1
    elif guess>answer:
        print('氣氣氣氣氣')
        b=guess
        c+=1
    else:
        print('yee')
        break
if c==5:
    print('辣雞')