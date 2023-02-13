g=input("enter the grade of employee")
if g == "A" or g == "B":
    print(g)
elif g != "A" or g != "B":
    print("enter valid grade")
n=int(input("enter the employee salary"))
if n <= 0 :
    print("enter a valid number")
elif(g ==  "A"):
   if n  >10000:
        bonus=n*0.05
        print("salary is " , n)
        print("bonus is " ,bonus)
        print("total to be paid",n+bonus)
   else:
        bonus=n*0.02
        print("salary is " , n)
        print("bonus is " ,bonus)
        print("total to be paid",n+bonus)

elif(g == "B") :
    if n > 10000:
        bonus=n*0.1
        print("salary is " , n)
        print("bonus is " ,bonus)
        print("total to be paid",n+bonus)
    else:
         bonus=n*0.02
         print("salary is " , n)
         print("bonus is " ,bonus)
         print("total to be paid",n+bonus)
