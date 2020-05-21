n=int(input("give number"))
if(n>1):
    print("2")
    for i in range(2,n):
        for j in range(2,i):
            if(i%j==0):
                break;
            elif(j==i-1):
                print(i)
else:
    print(("there is no prime number"))