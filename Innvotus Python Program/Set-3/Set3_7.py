import math
x=[80,79,82,78,81]
sum=0
for i in x:
    sum=sum+i
mean=sum/len(x)
v1=0
for i in x:
    v1=v1+math.pow((mean-i),2)
v1=v1/len(x)
sd=math.sqrt(v1)
min=mean-sd
max=mean+sd
print("Marks to obatain are=",min,"to",max)

