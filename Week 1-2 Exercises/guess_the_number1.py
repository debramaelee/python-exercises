secret_number = "5"

print "I am thinking of a number between 1 and 10"

switch = raw_input("What's the number? ")
while switch != "5":
    switch = raw_input("Nope, try again ")
print "Yes! You win!"
