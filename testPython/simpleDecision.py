inputName = input("What is your name? ")
inputAge = int(input("What is your age? "))

mature = False
if inputAge > 18:
    mature = True

if inputName.isprintable and mature:
    print("Your name is " + inputName)
    print("Your age is " + str(inputAge))
else    :
    print("Your name is " + inputName)
    print("Your age is " + str(inputAge) + " donot go to Kroad")

print("Thanks")

freeShip = False
inputTotal = int(input("How much is your total purchase ? "))

if inputTotal >= 50:
    freeShip = True

if freeShip:
    print("Your total purchase is " + str(inputTotal) + " and you have free shipping")
else:
    inputTotal +=10
    print("Your total purchase is " + str(inputTotal) + " $10 for Shipping is added")
