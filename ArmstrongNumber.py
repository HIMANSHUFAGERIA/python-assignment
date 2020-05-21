a=int(input("give number 1"))
b=0;
c=a;
while(c>0):
    b+=1;
    c=int(c/10);
sum=0
d=a;
while(d>0):
    r=d%10;
    sum=sum+r**b;
    d=int(d/10);
print(sum)
if(sum==a):
    print("armstrong")
else:
    print("not armstrong")