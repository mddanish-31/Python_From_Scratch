# write a program to accept marks of 6 students and display them in sorted manner

marks=[]

mark1=int(input("enter marks 1:"))
marks.append(mark1)
mark2=int(input("enter marks 2:"))
marks.append(mark2)
mark3=int(input("enter marks 3:"))
marks.append(mark3)
mark4=int(input("enter marks 4:"))
marks.append(mark4)
mark5=int(input("enter marks 5:"))
marks.append(mark5)
mark6=int(input("enter marks 6:"))
marks.append(mark6)
marks.sort()
print(marks)
