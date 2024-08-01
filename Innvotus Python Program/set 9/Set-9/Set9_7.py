x=[2,4,5,6,7,17,37]
count=0
for num in x:
        flag=True
        for i in range(2,num):
            if(num%i==0):
                flag=False
                break
        if(flag):
            count+=1
            print(num)
print("Number of Prime number are::",count)