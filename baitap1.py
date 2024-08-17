# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:21:58 2024

@author: User
"""

gpa = float(input("Nhập điểm trung bình"))
if gpa < 3.5:
    print("Học lực kém");    
elif gpa >= 3.5 and gpa < 5.0:
    print("Học lực yếu");
elif gpa >= 5.0 and gpa < 7.0:
    print("Học lực trung bình");
elif gpa >= 7.0 and gpa < 8.0:
    print("Học lực khá");
elif gpa >=8.0 and gpa <9.0:
    print ("Học lực giỏi");
else:
    print ("Học lực xuất sắc")
    