# 10. Write a program which takes the number of seconds as input & convert it into hours, minutes and seconds.
nos =4509 
Minutes =  (int)(nos/60) # (4509/60)= 75.15
Hours = (int)(Minutes/60) # 75.15/60 = 1.25 [1 hours ]
Minutes =  (int)(Minutes%60) # 75.15%60 = 15.15 [15 minutes ]
Seconds =(int)(nos%60) # (4509%60) = 4500 [ 9 seconds] remender = 9 beacuse 60*75 = 4500 

print("Hours =",Hours ," Minutes =",Minutes , " Seconds =",Seconds)
#  ANS: Hours = 1  Minutes = 15  Seconds = 9
