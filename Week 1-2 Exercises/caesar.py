
# old_letter_pos = ord('a')
# new_letter_pos = old_letter_pos + 13
# print chr(new_letter_pos)

secret_word = "hello"
offset = 13
alphabet = map(chr, range(97, 123))
alphabet_str = ''.join(map(str, alphabet))
result_str = ''

#for char in secret_word:
for char in secret_word:
    #to account for spaces, commas, etc
    if char not in alphabet_str:
        new_char = char
    else:
        idx = alphabet_str.find(char)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
            new_char = alphabet_str[new_idx]
    result_str += new_char

print result_str

# i = "hello"
# def convert_to_ascii(text):
#     return " ".join(str(ord(char)) for char in text)
#
# convert_to_ascii("hello")

#for char in word:
    #result_char = alphabet[index]
# old
# new
#
# .replace()
