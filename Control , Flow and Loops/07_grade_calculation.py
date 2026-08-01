# Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks=float(input("Enter the marks of the student: "))
if(marks>=90 and marks<=100):
    print("Grade of the student is Ex and marks is :",marks)
elif(marks>=80 and marks<90):
    print("Grade of the student is A and marks is :",marks)
elif(marks>=70 and marks<80):
    print("Grade of the student is B and marks is :",marks)
elif(marks>=60 and marks<70):
    print("Grade of the student is C and marks is :",marks)
elif(marks>=50 and marks<60):
    print("Grade of the student is D and marks is :",marks)
elif(marks<50):
    print("Grade of the student is F and marks is :",marks)