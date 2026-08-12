def greatest(a,b,c):
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=float(input("Enter third number: "))
    if a>b and a>c:
        print(f"{a} is the greatest number")
    elif b>a and b>c:
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")
greatest(0,0,0)