from sys import argv
script,codefile=argv
print(f"Hey there I am {script}")
print(f"Do you want me to delete {codefile}")
asking=input("Yes or no")
if asking=="Yes"or"yes":
    opener=open(codefile,'w')
    opener.truncate()
    print("Done*_*")
elif asking=="No"or"no":
    print("Okay:)")

asking=(input(f"Do you want to write in {codefile}"))

if asking=="Yes"or"yes":
    opener=open(codefile,"w")
    line1=input(">")
    line2=input(">")
    line3=input(">")
    opener.write(line1)
    opener.write(line2)
    opener.write(line3)
    print("Done0_o")
    opener.close()


