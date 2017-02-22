import random

def play_again():
    play_again = raw_input("Do you want to play again? (y or n) ")
    if play_again == "y":
        guess_num()
    else:
        print "Bye"

def guess_numb():
    count = 5
    secret_num = random.randInt(1, 10)
    print "I am thinking of a num between 1 - 10. You have %d guesses left" % count


    #continue after
