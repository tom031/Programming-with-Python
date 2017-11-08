inputName = input("What is your name? ")
inputAge = int(input("What is your age? "))

mature = False
if inputAge > 18:
    mature =True

if inputName.isprintable and mature:
    print("Your name is " + inputName)
    print("Your name is " + str(inputAge))
else    :
    print("Your name is " + inputName)
    print("Your name is " + str(inputAge) + " donot go to Kroad")

print("Thanks")
