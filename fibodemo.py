#Fibonacci Series

# 0  1   1   2   3   5   8   13  21 .....    
print("Program to Print Fibonacci Series")

num = int(input("Enter Number"))

f1 = 0 

f2 = 1

print(f1, " " , f2, end=" " )

f3 = f1 + f2 

while (f3<num):
    print(f3, end=" " )
    f1  = f2 
    f2 = f3 
    f3 = f1 + f2
    
    

    
 