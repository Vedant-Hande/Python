num=int(input("Enter the number :"))
flag=True
for i  in range(2,num):
    if(num%i==0):
        flag=False
        break
if(flag):
    print(num,"Is a prime number...")
else:
    print(num,"Is not a prime number...")
    