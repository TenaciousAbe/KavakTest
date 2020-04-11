def validator(x):
    result = ""
    if x%3 == 0:
        result = "A"
    if x%5 == 0:
        if result == "A":
            result = "Multiple of Both"
        else:
            result = "B"
    print ("Result: " + str(x) + ' = ' + result)

def altinput(message):
    while True:
        try:
            newinput = int(input(message))
        except ValueError:
            print ('Only 1 or 2!')
            continue
        else:
            return newinput
            break

action = altinput ("Automatic(1) or Manual(2) process? ")
if action == 1:
    for number in range(1, 101):
        validator(number)
elif action == 2:
    number = altinput ("Enter number between 1 to 100: ")
    if 1 <= number <= 100:
        validator(number)
    else:
        print ('Outside valid input!')
else:
    print ('Options are 1 or 2!')
