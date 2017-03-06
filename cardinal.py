# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:30:04 2017

@author: Melo Mtombeni
A program to write numbers cardinally
"""

def cardn(n):
    if(str(n)[-1]=='1'):
        print(str(n)+'st')
    elif(str(n)[-1]=='2'):
        print(str(n)+'nd')
    elif(str(n)[-1]=='3'):
        print(str(n)+'rd')
    else:
        print(str(n)+'th')        