#  Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)
s.add("18")
print(s,type(s))

#   yes we can have both 18 as an int and 18 as a string value in a set