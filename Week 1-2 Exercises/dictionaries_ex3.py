word = raw_input("What is your word? ")

counts = {}

# initial method
# for char in letter_histogram:
#     counts[char] = counts.get(char, 0) + 1
#
# for char, count in counts.items():
#     print "%s : %d" % (char, count)

#{'a': 3, 'b': 1, 'n': 2}
#dynamic keys

for char in word:
    if char not in counts:
        # add to dictionary
        counts[char] = 1
    else:
        counts[char] += 1

print counts
