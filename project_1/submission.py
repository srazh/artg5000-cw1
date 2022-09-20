#python script for chat bot that does math using a while loop, variables, and if statements
while(True):
    x = int(input("Please enter a number:"))
    y = int(input("Please enter another number:"))

    operation = String(input("What operation would you like to perform? You can add, subtract, divide or multiply"))

    if (operation = "add"):
        result = x + y
        print("The sum of x and y is " + result)
    elif (operation = "subtract"):
        result = x - y
        print("The difference of x and y is " + result)
    elif (operation = "multiply"):
        result = x * y
        print("The product of x and y is " + result)
    elif (operation = "divide"):
        result = x / y
        print("The quotient of x and y is " + result)
    
# script for chat bot that asks about your sleep utilizing a while loop and if statements
while(True):
    hours = int(input("How many hours of sleep did you get last night?"))
    if (hours < 1 or hours > 24):
        print ("Not a valid input.")
    if (0 < hours <= 3):
        print("wow I think you need to get more sleep!")
    if (4 < hours <= 7):
        print("did you have an essay due today or something?")
    if (8 < hours <=10):
        print("That is the perfect amount of sleep!")
    if (11 <hours <=24):
        print("it's not winter yet, why are you hibernating?")
