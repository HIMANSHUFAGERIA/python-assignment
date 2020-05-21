rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if(j==0 or j==rows-1 or i==j and i>=int(rows/2) or i+j==rows-1 and i>=int(rows/2)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();