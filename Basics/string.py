# String is a sequence of character containing in double as well as in single quote.
str1 = "Garv Anand"
str1Len = len(str1)
# print(str1Len)

# String Slicing is define as cutting of string with usefull string character.
# example
str2 = "!Mango!!!!!!!!!!"
# print(str2[0:4])

# Here it contain the character starting from the index 0 upto index 4 but also not contain the 4th index element
# print(str2[0:-3])

# Understand more string functions
# 1. upper()
# Making our string in pure uppercase only
print(str2.upper())  

# 2.lower()
# Making our string in pure lowercase only
print(str2.lower())

# 3.rstrip()
# Remove the symbols form last not form beginning
print(str2.rstrip("!"))
