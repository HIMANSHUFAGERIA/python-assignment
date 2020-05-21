rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if( i==rows-1 and j<=int(rows/2) or j==0):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();