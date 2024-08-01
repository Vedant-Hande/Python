num=1234
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=int (num/10)
print("SUM=",sum)