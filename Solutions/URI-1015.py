# URI Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1015
# Programmed by Marufur Rahman.
##Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = 

Input

The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

Output

Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.

Input Sample

1.0  7.0
5.0  9.0

Output Sample

4.4721


#Solution : 



var1 = input().split(" ")
var2 = input().split(" ")

x1,y1 = var1
x2,y2 = var2

distance = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %distance)
