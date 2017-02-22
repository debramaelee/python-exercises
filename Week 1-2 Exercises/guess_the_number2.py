secret_number = 5

print "I am thinking of a number between 1 and 10"

switch = int(raw_input("What's the number? "))
while switch != 5:
    if switch < 5:
        switch = int(raw_input("%d is too low. What's the number? " % switch))
    elif switch > 5:
        switch = int(raw_input("%d is too high. What's the number? " % switch))
print "Yes! You win!"
