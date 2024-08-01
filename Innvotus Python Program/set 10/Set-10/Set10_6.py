import array as  arr
a=arr.array('i',[1,2,3,4,5,6,7,8,9])
print("Input Array before swapping Big and Small")
for i in a:
    print(i)

big=a[0]
small=a[0]
bp=0
sp=0
for i in range(len(a)):
    if(a[i]>big):
        big=a[i]
        bp=i
    if(a[i]<small):
        small=a[i]
        sp=i

print("Big = ",big)
print("Small = ",small)

temp=a[bp]
a[bp]=a[sp]
a [sp]=temp

print("Out Array after swapping Big and Small")
for i in a:
    print(i)
