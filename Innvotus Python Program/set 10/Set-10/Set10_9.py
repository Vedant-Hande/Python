import array as arr
a=arr.array('i', [23, 65, 78, 90, 21, 34, 9, 2])
element=int(input("Enter the element to be Search :"))
pos =- 1
for i in range(len(a)):
    if(element == a[i]):
        pos=i
        break
if(pos ==- 1):
    print(element," is NOT found in the array ")
      
else:
    print(element," is found in the array at the position ",pos)
       





