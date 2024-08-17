# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:31:17 2024

@author: smai
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b + c > 0 and a + b > c and a + c > b and b + c > a:
   if a == b == c:
       print ("Tam giác đều")
   elif a == b or a == c or b == c:
        print ("Tam giác cân")
   elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print ("Tam giác ")     
   else:
        print ("Tam giác thường")
else:
    print ("3 cạnh này không phải là 3 cạnh của 1 tam giác")
    
    
