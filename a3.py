p = int(input("Enter the maximum marks of a subject"))
d = int(input("Enter your marks : "))
grade = int(input("Enter your marks : "))
c = int(input("Enter your marks : "))
b = int(input("Enter your marks : "))
a = int(input("Enter your marks : "))
sum = grade+d+a+b+c
avg=sum / 5
totalmarks= p*5
percentage = sum/totalmarks*100
print("percentage is" , percentage )

print("your average is" , avg)
if avg>90 :
    print("you got grade A1")
elif avg>80 :
    print("you got grade B1")
elif avg>70 :
    print("you got grade C1")
elif avg>60 :
    print("you got grade D1")
elif avg>50 :
    print("you got grade E1")
else:
    print("you have failed")