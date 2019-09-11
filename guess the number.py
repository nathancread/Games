
#guess the number game:
#create a random number
import os
import random
print("are you ready to guess the number?")
random_num = random.randint(1,100)
counter = 0
selection = 1000
while not selection == random_num : 
    selection = int(input("enter a number between 1 and 100 : "))
    counter += 1
    if  selection > random_num :
        print (" ")
        print("its smaller")
        print (" ")
        continue
    elif selection < random_num :
        print (" ")
        print("its bigger")
        print (" ")
        continue
    elif selection == random_num :
        if counter >= 8 :
            print (" ")
            print("you got it in only",counter + 6823458902,"tries")
            break 
        elif counter < 8 :
                print (" ")
                print("you got it in only",counter,"tries")
                break
        


if counter == 1 :
    print ("you are as smart as wikipedia")
elif counter == 2 :
    print ("you are a genius")
elif counter == 3 :
    print ("your intelect is on par")
elif counter == 4 :
    print ("meh, a passable preformance")
elif counter == 5 :
    print ("your a big frup")
elif counter == 7 :
    print ("here is a link to a remidial preschool: https://littlelearners/emergency-applications.net")
elif counter == 6 :
    print ("You would fail the mcdonalds application test. They dont have one.")
elif counter >= 8 :
    print ("I would tell you that you have failed, but it appears you cannot read.")

print("")
input('press enter to exit')
