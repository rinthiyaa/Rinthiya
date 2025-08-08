#Problem-3
a=int(input("Enter a number:"))
if a%2==0:
    a=a-1
for i in range(a):
    res=2*i+1
    print(res,end=",")
