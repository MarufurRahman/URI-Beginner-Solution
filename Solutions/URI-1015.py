# URI Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1015
# Programmed by Marufur Rahman.

import math

var1 = input().split(" ")
var2 = input().split(" ")

x1,y1 = var1
x2,y2 = var2

distance = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %distance)