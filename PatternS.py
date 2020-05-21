rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if(j==0 and i<=int(rows/2) or j==0 and i>=int(3*rows/4)  or j==rows-1 and i>=int(rows/2) or j==rows-1 and i<=int(rows/4) or i==0 or i==rows-1 or i==int(rows/2)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();