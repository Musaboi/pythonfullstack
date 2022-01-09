#asking temperature
temperature = int(input("What's the temperature:"))
#asking in what to convert
converter= str(input("Do you want to convert it into c for celcius or f for farenheit:"))
if converter=="c" or converter=="C":
    print(int((temperature-32) * 5/9),"°F")
elif converter == "F" or converter=="f":
    print(int((temperature * 9/5) + 32),"°C")
