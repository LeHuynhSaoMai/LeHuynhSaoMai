# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:45:19 2024

@author: smai
"""

a = float(input("Nhập a ="))
b = float(input("Nhập b ="))
if a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Ngiệm của phương trình là x =", (-b/a))
    