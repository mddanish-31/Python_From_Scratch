# a=int(input("Enter a number: "))
# if(a%2==0):
#     print("a is even")
# else:
#     print("a is odd")

#calculate the fahrenheit from celsius
# celsius=float(input("Enter temperature in celsius: "))
# fahrenheit=(celsius*9/5)+32
# print("Temperature in fahrenheit is: ",fahrenheit)

#sum of digits of a number
# a=int(input("Enter a number: "))
# sum=0
# while(a>0):
#     digit=a%10
#     sum=sum+digit
#     a=a//10
# print("Sum of digits is: ",sum)

#add two numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sum=a+b
# print("Sum of two numbers is: ",sum)

#leap year or not
# year=int(input("Enter a year: "))
# if(year%4==0 and year%100!=0) or (year%400==0):
#     print(year,"is a leap year")

#find the max,min number among three numbers
# Find the maximum and minimum among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding maximum
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

# Finding minimum
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print("Maximum number is:", maximum)
print("Minimum number is:", minimum)