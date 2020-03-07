# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:50:28 2020

@author: sami
"""

import random
answer=random.randint(1,50)
a=  1
b=50


while True:
    guess=input(str(a)+'~'+str(b)+'猜數字，猜錯我就罵你可憐哪')
    guess=int(guess)
    
    if guess<answer:
        print('可憐哪')
        a=guess
    elif guess>answer:
        print('氣氣氣氣氣')
        b=guess
    else:
        print('yee')
        break