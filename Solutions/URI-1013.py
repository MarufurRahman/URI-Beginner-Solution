# URI Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1013
# Programmed by Marufur Rahman.

import math

value = input().split(" ")
a, b, c = value

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
result = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" %result)