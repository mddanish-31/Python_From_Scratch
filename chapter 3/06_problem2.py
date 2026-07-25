letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

print(letter.replace("<|Name|>","md danish raza").replace("<|Date|>","25-07-2026"))
# print(letter.replace("<|Date|>","25-07-2026")) # it will not work since the name section will not work