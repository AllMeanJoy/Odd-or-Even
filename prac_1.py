prompt = input("What number is on your mind? ")

try :
    num = int(prompt)
    if num > 1000:
        print("Please enter a number 0-1000!")
    elif num < 0:
        print("Please enter a number 0-1000!")
    elif num %2 == 0:
        print("Sweet, that's an even number!")
        print("Thank You, May I have another?")
    else :
        print("That's an odd one!")
        print("Thank You, May I have another?")
except :
    print("Please enter a number 0-1000!")
