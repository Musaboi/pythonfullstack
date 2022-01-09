#Asking the user to type a number
guessing = int(input("Guess a number:"))
#having a loop so that if the user types any other thing the code re-runs
while guessing>= 10:
    guessing = int(input("Guess a number:"))
#if statements to meet the conditions
if (guessing)<1 or int(guessing)>9:
    guessing = input("Guess a number:")

elif (guessing)>=1 and (guessing)<=9:
    print("Well guessed!")


