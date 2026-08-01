# Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.
marks1=int(input("enter 1st subject marks "))
marks2=int(input("enter 2nd subject marks "))
marks3=int(input("enter 3rd subject marks "))

total_percentage=(100)*(marks1+marks2+marks3)/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed :",total_percentage)
else:
    print("you are failed :",total_percentage)
# if(a1<33):
#     print("student has failed")
# else:
#     print("student had passed in the subject")
# if(a2<33):
#     print("student has failed")
# else:
#     print("student had passed in the subject")
# if(a3<33):
#     print("student has failed")
# else:
#     print("student had passed in the subject")
