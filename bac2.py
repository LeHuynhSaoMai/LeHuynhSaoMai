# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:07:12 2024

@author: smai
"""



# Nhập các hệ số 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x =", -b/(2*a))
else:
    print("Phương trình có hai nghiệm phân biệt", (-b + delta**0.5)/(2*a), "và", (-b + delta**0.5)/(2*a))
   

   