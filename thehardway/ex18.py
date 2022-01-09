def print_one(*args):
    arg1,arg2=args
    print(f"arg1:{arg1},arg2:{arg2}")

def print_one_better(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

def print_two(arg1):
    print(f"arg1:{arg1}")

def print_toe():
    print("Hi,I am toe!")

print_one(1,2)
print_one_better("better1","better2")
print_two("One")
print_toe()
