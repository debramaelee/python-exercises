x = raw_input("What is your string? ")

# x = x.replace("aa","aaaaa")
# x = x.replace("ee","eeeee")
# x = x.replace("ii", "iiiii")
# x = x.replace("oo", "ooooo")
# x = x.replace("uu","uuuuu")
#
# print x

# correct method

for i in range(len(x)):
    two_letters = x[i:i+2]
    if two_letters == 'oo':
        result += 'ooooo'
    elif two_letters == 'ee':
        result += 'eeeee'
    else:
        result += x[i]

print result
