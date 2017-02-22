word_histogram = raw_input("Insert a paragraph of text. ")
word_split = word_histogram.split()

counts = {}

# for word in word_split:
#     counts[word] = counts.get(word, 0) + 1
# for word, count in counts.items():
#     counts.append(word, counts)
# print counts

# for word, count in counts.items():
#     print "%s : %d" % (word, count)


def word_histogram(sentence):
    words = sentence.split()
    current_word = ""
    word_lib = {}

    for word in word_list:
        if word not in word_lib:
            word_lib[word] = 1
        else:
            word_lib[word] += 1
    print word_lib
