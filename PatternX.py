rows = int(input("Enter the number of rows "))
for i in range(0,rows):
    for j in range(0,rows):
        if((i==j or i+j==rows-1) ):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print();