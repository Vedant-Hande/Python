x=[-1,0,67,89,0,-12,-5,0,0,0,87,45]
zc,pc,nc=0,0,0
for element in x:
    if(element>0):
        pc+=1
    elif (element<0):
        nc+=1
    else:
        zc+=1
  
print("Zero count = ",zc)
print("Positive count= ",pc)
print("Negative Count = ",nc)