rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if(i==0 and j<=int(rows/2) or j==0 or i==rows-1 and j<=int(rows/2) or i==int(rows/2) and j<=int(rows/2)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();