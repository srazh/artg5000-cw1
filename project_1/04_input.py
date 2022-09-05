# This example uses the Python strip method: https://www.w3schools.com/python/ref_string_strip.asp

name = input("What is your name?")
# Create an infinite while loop that continues until there is a break
while True:
	if name.isnumeric():
		print("I'm sorry, numbers are not accepted as names")
		break
	else:
		print("Hello, "+ name)

	grade = input("What grade do you hope to get in this class?")
	# Remove any + or - using the python strip() method
	grade = grade.strip("+-")
	if grade.lower() == "a":
		print("That is pretty ambitious, but you can do it if you put your mind to it!")
		break
	elif grade.lower() == "b":
		print("That's good, but why not an 'A'?")
		break
	elif grade.lower() == "c":
		print("Well, we can't all be overachievers, I suppose...")
		break
	elif grade.lower() == "d":
		print("Really? That is what you hope to get?")
		break
	elif grade.lower() == "f":
		print("I'll assume that is because you like the class so much, you want to take it again.")
		break
	else:
		print("That's not a grade!")
		break


### But, what happens if the user enters a grade and a plus or minus?
