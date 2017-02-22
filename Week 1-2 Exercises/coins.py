#response = raw_input("Do you want a coin? ")

num_coins = 0
print "You have %d coins" % num_coins
switch = raw_input("Do you want another? (yes/no) ")
while switch == "yes":
    num_coins += 1
    print "You have %d coins." % num_coins
    switch = raw_input("Do you want another? (yes/no) ")
print "Bye"

# previous attept
#while (response == True):
#    if (response == "yes"):
#        print "Here is a coin for you"
#        num_coins += 1
#    else:
#        print "Byebye"

# alternative method
count = 0
print "You have %d coins" % count

while True:
    question = raw_input("Do you want another?")
    if question == "yes":
        count += 1
        print "You have %d coins" % count
    elif question == "no":
        print "Bye"
        break
