def args(*var):
    script,codefile = var
    print(f"Hi I am {script}")
    asking=input(f"Do you want to erase {codefile} ")
    if asking =="Yes" or "yes":
        opener = open(codefile,"w")
        opener.truncate()
        print("Done")
    elif asking== "No" or "no":
        print("ok")

    ask = input("Would you like write in that file")
    if ask == "yes":
        line1 = (input(">"))
        line2 = (input(">"))
        line3 = (input(">"))
        opener = open(codefile, "w")
        opener.write(line1)
        opener.write("\n")
        opener.write(line2)
        opener.write("\n")
        opener.write(line3)
        opener.close()
        print("Done")
    elif ask == "no" or "No":
        print("Ok:)")

args("ex18.py","ex15_sample.txt")
