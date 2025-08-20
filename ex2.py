# Create a string made of the middle three characters

s1 = input("Enter String")

mid = int(len(s1)/2)

newstr = s1[mid-1] + s1[mid] + s1[mid+1]

print(newstr)