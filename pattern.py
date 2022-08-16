a = 8 
num = 0
for i in range(0, 4): #number of lines in the triangle
    for j in range(0, a): #loop to mirror the right triangle
        print(end=" ")
    a = a - 2
    for j in range(0, i+1): #loop of the numbers in the triangle
        num = num + 1
        print(num, end=" ")
    print()
