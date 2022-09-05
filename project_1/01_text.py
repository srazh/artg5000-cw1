# Working with text in Python
# See: https://www.w3schools.com/python/python_strings.asp
# See also: https://docs.python.org/3/library/string.html

# Text in Python is called a string.
# To make a string, put text or numbers inside quotes
print("I am a string!")

# strings can be assigned to a variable
s = "This string is a variable.... "
print(s)

# strings can be added to each other
new_s = "and this is more stuff to add."
print(s+new_s)

# You cannot add numbers with strings, 
# but you can change numbers into strings with str()
num = 123456789
print(s+str(num))

# You can use single or double quotes to make a string
single_quote = 'This is a single quote string'

# If you need to have a quotation inside of a string, 
# you can escape the character with a backslash \
quote = "It was Descartes who said \"I think, therefore I am\""
print(quote)

# Large quotes can be written using 3 quotes
lg_quote = '''It seems probable that once the machine thinking method had started, it would not take long to outstrip our feeble powers... They would be able to converse with each other to sharpen their wits. At some stage, therefore, we should have to expect the machines to take control. - Alan Turing'''

print(lg_quote)

# A return carrage, or new line, can be made using a backslash and n \n
new_line = "This is a line.\nAnd this is another line."
print(new_line)

# Strings are also arrays that can be iterated through
for letter in "word":
	print(letter)

# You can find out how many characters are in a string by using len()
print("the large quote is: ", len(lg_quote), " characters long.")

# You can check if a word is in a string like any other array
if "machine thinking" in lg_quote:
	print("Found machine thinking!")

# You can change the case of a string with upper() and lower
print(quote.upper())
print(quote.lower())
