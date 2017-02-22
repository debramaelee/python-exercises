import random
my_random_number = random.randint(1, 10)

print "I am thinking of a number between 1 and 10"

switch = int(raw_input("What's the number? "))
tries = 5

while True:
    if switch < my_random_number:
        tries -= 1
        print "You have %r tries left!" % tries
        switch = int(raw_input("%d is too low. What's the number? " % switch))
    elif switch > my_random_number:
        tries -= 1
        print "You have %r tries left!" % tries
        switch = int(raw_input("%d is too high. What's the number? " % switch))
    else:
        print "Yes! You win!"
        break
    if tries <= 1:
        print "You ran out of guesses!"
        break
