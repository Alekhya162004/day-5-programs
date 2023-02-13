from math import factorial
n = int(input("enter the number of rows:"))
if(n<=0):
    print("Enter a positive number")
n2=int(input("enter  a row number:"))
if(n2<=0):
    print("Enter a positive number")
s=0
for i in range(n):
    for j in range(n-i+1):

        print(end=" ")

    for j in range(i+1):
            a=(factorial(i)//(factorial(j)*factorial(i-j)))
            if n2==i+1:
                s=s+a

            print(a,end=" ")
    print()
print()
print(s)
