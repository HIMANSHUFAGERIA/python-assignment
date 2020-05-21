rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if(i==0 or j==int(rows/2)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();