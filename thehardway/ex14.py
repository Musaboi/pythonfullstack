from sys import argv
script,user_name = argv
prompt ='>'
print(f"Hi {user_name},I'm the {script} script.")
print(f"I'd like to ask few question.")
print(f"Do you like ice-cream,{user_name}?")
ice_cream=input(prompt)
print("What kind of computer you have?")
computer=input(prompt)
print(f"So you said \"{ice_cream}\" about liking ice-cream\nand you have a {computer} 0_o computer.It's cool:).")
#IF YOU CAN'T RUN THIS THEN GO TO YOUR RUN IN THE BAR AT THE TOP AND THEN RIGHT CLICK THEN GO TO EDIT CONFIGURATIONS AFTER THAT TICK THE RUN WITH PYTHON CONSOLE.
#THEN APPLY AFTER THAT OPEN YOUR TERMINAL IN PYCHARM THEN ENTER /\ python ex14.py {your name} /\