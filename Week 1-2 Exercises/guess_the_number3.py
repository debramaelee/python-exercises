import random
my_random_number = random.randint(1, 10)

print "I am thinking of a number between 1 and 10"

switch = int(raw_input("What's the number? "))
while switch != my_random_number:
    if switch < my_random_number:
        switch = int(raw_input("%d is too low. What's the number? " % switch))
    elif switch > my_random_number:
        switch = int(raw_input("%d is too high. What's the number? " % switch))
print "Yes! You win!"
