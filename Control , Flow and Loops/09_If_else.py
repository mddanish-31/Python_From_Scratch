apple=int(input("Enter the price of apple: "))
mango=int(input("Enter the price of mango: "))
cart=apple+mango
budget=300
if(cart<=budget):
    print("You can buy the fruits")
else:
    print("You cannot buy the fruits")