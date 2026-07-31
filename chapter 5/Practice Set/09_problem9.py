# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}
s=[4][0]=9 # it will shoe a TypeError since a list cannot be present in a set since list are mutable and unhashable
print(s)


# No. 
# A list cannot be an element of a set because lists are mutable and unhashable. 
# Hence, the given set is invalid and raises a TypeError.