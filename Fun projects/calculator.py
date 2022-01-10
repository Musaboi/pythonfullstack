a = int(input("Enter any number"))
b= int(input("Enter another number"))
def add(a,b):
    print(f"Your answer is {a+b}")

def subtract(a,b):
    print(f"Your answer is {a-b}")

def multiply(a,b):
    print(f"Your answer is {a}*{b} ")
    return a*b

def divide(a,b):
    print(f"Your answer is {a/b}")
    return a/b

calculator= input("Do you want to + for add, - for subtract, * for multiply or / for divide")

if calculator =="+":
    add(a,b)
elif calculator == "-":
    subtract(a,b)
elif calculator == "*":
    multiply(a,b)
elif calculator =="/":
    divide(a,b)
