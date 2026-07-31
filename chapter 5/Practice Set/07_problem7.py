# #  If the names of 2 friends are same; what will happen to the program in problem 6?

# #  Create an empty dictionary. 
# # Allow 4 friends to enter their favorite language as value and use key as their names. 
# # Assume that the names are unique.

d={}
name=input("enter friend name :-")
lang=input("enter language name:-")
d.update({name:lang})
name=input("enter friend name :-")
lang=input("enter language name:-")
d.update({name:lang})
print(d,type(d))

# if the two names are same it will be taken 1 time
# values can be same it will be updated if 2 keys of same name taken with 2 different value
# the last value will be taken with 1 unique  key
# nothing happens the values can be same 


