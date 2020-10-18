#Program Maded by Adi --- 14/9/2020
#All Rights Reversed
#45 * 3= 555, 56+9= 77, 56/6= 4
#THIS CALCULATOR IS FAULTY
print("Welcome To The Python Calculator - Developed By Adi\n")


print("Which Thing You Want to Do\n")
print("Type + for Addition")
print("Type - for Subtraction")
print("Type / for Division")
print("Type * for Multiplication")
print("Type ** for Power\n")

operator=input()

print("------Please Enter Numbers Only------\n")

print("Enter First Number")
num1=int(input())
print("Enter Second Number")
num2=int(input())
if operator=='+' and num1==56 and num2==9:
    print("77")

elif operator=='*' and num1==45 and num2==3:
    print("555")

elif operator=='/' and num1==56 and num2==6:
    print("4")

elif operator== '+':
    plus=num1+num2
    print(plus)

elif operator=='-':
    minus=num1-num2
    print(minus)

elif operator=='/':
    divide=num1/num2
    print(divide)

elif operator=='*':
    multiply=num1*num2
    print(multiply)

elif operator=='**':
    power=num1**num2
    print(power)

else:
    print("Wrong Input Please Check your Input\n")


print("Thanks For using my Calculator")
print("Hope You Will Have Your Answer\n")

print("Press any Key To Exit")
exitprog=input()
