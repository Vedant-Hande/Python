x=[10,20,30,40,50]
k=bytearray(x)
print("Before update==")
for i in k:
     print(i)
print("After update==")
k[0]=100
k[3]=200
for i in k:
     print(i)