# This code is about Regular Expressions: https://www.w3schools.com/python/python_regex.asp
'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
'''
# Import RegEx like this:
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# An empty list is returned if nothing is found
p = re.findall("Portugal", txt)
print(p)

# Regular expressions can also be used for string manipulations
# Split breaks the text at each occurance, such as a space:
s = re.split(" ", txt)
print(s)

# You can also substitute characters or words using re.sub
# The first paramiter what to replace, the second is what to replace it with, and the third is the text to perform the replacement on.
b = re.sub("Spain", "Boston", txt)
print(b)