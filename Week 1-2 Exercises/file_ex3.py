# Write a program that prompts the user to enter a file name,
# then prints the letter histogram and the word histogram of
# the contents of the file.

myfile = raw_input("What is the name of your file? ")
myfile = open(myfile)


counts = {}

for char in myfile:
    if char not in counts:
        # add to dictionary
        counts[char] = 1
    else:
        counts[char] += 1
print counts

# def word_histogram(myfile):
#     words = myfile.split()
#     current_word = ""
#     word_lib = {}
#
#     for word in myfile:
#         if word not in word_lib:
#             word_lib[word] = 1
#         else:
#             word_lib[word] += 1
#     print word_lib
#
# print word_histogram(myfile)
