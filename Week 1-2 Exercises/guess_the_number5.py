import random
my_random_number = random.randint(1, 10)

play_again = "y"

print "I am thinking of a number between 1 and 10"

switch = int(raw_input("What's the number? "))
tries = 5

while True:
    while play_again == 'y':
    if switch < my_random_number:
        tries -= 1
        print "You have %r tries left!" % tries
        switch = int(raw_input("%d is too low. What's the number? " % switch))
    elif switch > my_random_number:
        tries -= 1
        print "You have %r tries left!" % tries
        switch = int(raw_input("%d is too high. What's the number? " % switch))
    else:
        play_again = raw_input("Yes! You win! Do you want to play again? (y/n)")
        break
    if tries <= 1:
        print "You ran out of guesses!"
        break


#using function
#def play_again()
