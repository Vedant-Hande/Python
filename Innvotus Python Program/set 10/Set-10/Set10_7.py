import array as  arr
a=arr.array('i',[1, -2, 3, 0, -1, 0, 5, 0, -3])
positives = 0
negatives = 0
zeros = 0
for num in a:
    if num > 0:
        positives += 1
        
    elif num < 0: 
        negatives += 1
       
    else:
        zeros += 1       

print("Positive numbers:",positives)
print("Negative numbers:",negatives)
print("Zeros:",zeros)
