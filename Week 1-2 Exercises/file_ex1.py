# 1. Write a program that prompts the user to enter a file name,
# reads the contents of the file and prints it to the screen.

myfile = raw_input("What is the name of your file? ")
myfile = open(myfile)

file_lines = myfile.readlines()

for i in range(len(file_lines)):
    print "line %d: %s" % (i + 1, file_lines[i])
