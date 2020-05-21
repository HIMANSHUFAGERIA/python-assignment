a=int(input("give number "))
b=0;
while(a>0):
    c=a%10;
    b=b*10+c;
    a=int(a/10);
print(b)
if(a==b):
    print("Palindrome")
else:
    print("not palindrome")