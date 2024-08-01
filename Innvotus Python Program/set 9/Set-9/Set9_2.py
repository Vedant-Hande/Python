import math
n=20
sum=0
for i in range(1,n+1):
    sum=sum+i
mean=sum/n
print("MEAN=",mean)
var=0
for i in range(1,n+1):
    var=var+math.pow((mean-i),2)
var=var/n
sd=math.sqrt(var)
print("SD=",sd)
min=mean-sd
max=mean+sd
print("Minimum Range::",min)
print("Maximum Range::",max)
print("Element in the range of min and max are::")
for i in range(1,n+1):
    if(i>=min and i<=max):
        print(i)
    