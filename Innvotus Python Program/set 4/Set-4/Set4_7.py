a=25
b=25
print("Address of a=",id(a))
print("Address of b=",id(b))
if a is b:
    print("Sharing a same address")
else:
    print("Not Sharing a same address")
