#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 00:10:32 2025

@author: linyixuan
"""

number=int(input("請輸入一個0-255的數字："))

#二進位
def binary(n):
    
    a = ""
    
    if n == 0:
        return "0"
    
    while n>0:
        r = n%2
        a=str(r)+a
        n=n//2
    return a

obinary=binary(number)

print(f"二進位： {obinary} ")

#十六進位
def hexa(n):
    
    listt ="0123456789ABCDEF"
    b = ""
    
    if n==0:
        return "0"
    
    while n>0:
        r=n%16
        b=listt[r]+b
        n=n//16
        
    return b

ohexa=hexa(number)

print(f"十六進位：{ohexa}")

    