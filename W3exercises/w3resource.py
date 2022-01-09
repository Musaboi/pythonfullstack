# Please add question in the file so that others who are reading gets a context
# Please move the Files Under Appropriate folder (Come up with folder structure {may be Excercises/ Scratchpad/ Musa})-"DONE😄"

number = int(input("Type a number:"))

# We are converting number to int at almost every three line
# What about converting it once and using it multiple times? - food for thought :)-"DONE😄"

if (number) < 1500 or (number) > 2700:

    # Try to read PEP 8 convention https://www.python.org/dev/peps/pep-0008/
    # Read it as much as you can no pressure

    print("The number you have type is less 1500 or bigger than 2700")
    number = input("Type a number:")
elif (number)%5==0 and (number)%7==0 :

    # do you really understand what "==" means, I recommend https://chercher.tech/python-questions/double-equalto-operator-python-questions#:~:text=The%20%3D%3D%20operator%20is%20a,%2C%20tuples%2C%20dictionaries%2C%20etc.
    # ^^ I broke PEP 8 convention in above line, find out why?

    print("The number is divisible by 7 and multiple of 5")
elif (number)%5 == 0:
    print("The number is a multiple of 5 ")
elif (number)%7 == 0:
    print("The number is divisible by 7 ")
elif (number) >= 0 :
    print("The number isn't divisible by 7 or multiple of 5")
elif (number)%5 == 0 and (number)%7 == 0:
    print("The number is divisible by 7 and multiple of 5")
