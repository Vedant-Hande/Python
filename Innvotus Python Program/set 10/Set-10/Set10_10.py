x=[2,3,5,7,9] 
y=[4,5,7,10,15]
expected_sunshine=8 
sumx=0
sumy=0
sumxy=0
sumx2=0
for i in range(len(x)):
    sumx=sumx+x[i]
    sumy=sumy+y[i]
    sumxy=sumxy+(x[i]*y[i])
    sumx2=sumx2+(x[i]*x[i])
print("sumx =",sumx)
print("sumy = ",sumy)
print("sumxy =",sumxy)
print("sumx2 =",sumx2)
n=len(x)
nr=n*sumxy-sumx*sumy
dr=n*sumx2-sumx*sumx
m=nr/dr
print("SLOPE (M) : ",m)

b=(sumy-m*sumx)/n
print("INTERCEPT (B) =",b)

y=m*expected_sunshine+b
print("Number of Ice creams to be sold for ",expected_sunshine, " hour of Sunshine is",y)
