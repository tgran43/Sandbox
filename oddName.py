"""Trey Grant"""
name = input('Please enter your name: ')
while name == "":
    name = input('Please enter your name: ')
print(name[1::2])