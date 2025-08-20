#whiledemo --Factorial 


num = int(input("Enter Value"))



fact = 1 
i= 1
while(i <= num):
    fact = fact * i 
    i = i + 1
     
     
     
print("  Factorial of ", num , " = ", fact )

'''
num         i       fact    cond i<=num 
4           1           1       T 
4           2           2       T 
4           3           6       T 
4           4           24      T 
4           5 
''' 