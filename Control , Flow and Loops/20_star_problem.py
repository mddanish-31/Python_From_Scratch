'''Write a program to  print the following star pattern. 

  * 
 **
***
for n = 3  '''
a=int(input("enter the number"))
for i in range(1,a+1):
#  print(" "* (a-i),end="")
 print("*"*(i),end="")
 print("")
