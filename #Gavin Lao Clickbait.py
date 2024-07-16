#Gavin Lao Clickbait

#Init
import random as r
#Functions
def Name():
    name = input("Enter a name: ")
    return ("You won't believe what" + " " + name + " " + "did on June 21st")
def Number():
    num = input("Enter a number: ")
    return (num + ' ' + 'LIFE HACKS THAT COULD MAKE YOU A MILLIONARE IN' + ' ' +     num + ' ' + 'DAYS'
            )
def Animal():
    animal = input("Enter an Animal: ")
    return ("A" + ' ' + animal + ' ' + 'is smarter than humans and this video will tell you why.')
def Youtuber():
    youtuber = input("Enter your favorite youtuber: ")
    return ("THIS WEBSITE CALLS" + ' ' + youtuber + ' ' + "AND YOU WON'T BELIEVE WHAT HAPPENED!")
def restaurant():
    restaurant = input("Enter the best restaurant: ")
    return ("THIS" + ' ' + restaurant + ' ' + 'HAS THE CRAZIEST SECRET MENU AND YOU WONT BELIEVE WHAT I FOUND')
def Generator():
    generate = r.randint(1,5)
    if generate == 1:
        print(Name())
    elif generate == 2:
        print(Number())
    elif generate == 3:
        print(Animal())
    elif generate == 4:
        print(Youtuber())
    else:
        print(restaurant())
#Main
Generator()
