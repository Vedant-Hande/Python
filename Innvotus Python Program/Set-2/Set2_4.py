import math
x1,y1,x2,y2,x3,y3=5,6,2,9,14,15
a=(math.pow((x1-x2),2)+math.pow((y1-y2),2))
b=(math.pow((x2-x3),2)+math.pow((y2-y3),2))
c=(math.pow((x1-x3),2)+math.pow((y1-y3),2))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area is=",area)
        
        