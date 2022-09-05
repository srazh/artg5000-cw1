# you can create an input like this:

name = input("What is your name?")
grade = input("What grade do you want in this class?")

# The output can be formatted using brackets {}
output = "Hello, {}, it is nice to meet you. I'm sure you will get a {} in the class."
# The variables will be inserted in the order they are entered
print(output.format(name, grade))

### Notice that the user can enter anything as a name or grade.
# Their name can be a number and their grade could be a "K"