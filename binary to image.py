# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:34:11 2024

@author: acer
"""

with open('new1.png','rb')as file:
    data=file.read()
with open('new2.png','wb')as file1:
    file1.write(data)