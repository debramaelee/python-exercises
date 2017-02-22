x = raw_input('Do you want to play again (Y or N?) ')

def f(x):

    if x == 'Y':
        return True
    elif x == 'N':
        return False
    else:
        x = raw_input('Invalid input. Try again ')

print f(x)
