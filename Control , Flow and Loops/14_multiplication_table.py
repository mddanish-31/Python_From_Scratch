#Write a program to print multiplication table of a given number using for loop.
table=int(input("enter the number for multiplication:"))
for i in range(1,11):
 print(table,"x",i,"=",table*i)