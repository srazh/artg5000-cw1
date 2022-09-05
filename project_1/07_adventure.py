# This code opens a file: https://www.w3schools.com/python/python_file_open.asp
# And saves it as a new file: https://www.w3schools.com/python/python_file_write.asp

import re

# Open the file --> "r" means read only
file = open("texts/wonderland.txt", "r")
wonderland = file.read()

name = input("Who's adventure is this?")
rabbit = input("Who will be the rabbit?")
cat = input("who will play the cat?")

#print(wonderland)
new_adventure = re.sub("Alice", name, wonderland)
new_adventure = re.sub("Rabbit", rabbit, new_adventure)
new_adventure = re.sub("Cheshire", cat, new_adventure)

print('\n\n*****'+name+"'s Adventure\n\n")
print(new_adventure)

# Save the file:
with open('texts/new_adventure.txt', 'w') as f:
	f.write(new_adventure)