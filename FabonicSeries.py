i=int(input("give number"))
a=0;
b=1;
c=1;
print(a,b,end=" ")
while(c<i):
    print(c,end=" ")
    a=b;
    b=c;
    c=a+b;