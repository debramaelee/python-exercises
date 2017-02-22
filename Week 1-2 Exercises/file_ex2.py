# Write a program that prompts the user to enter a file name,
# then prompts the user to enter the contents of the file,
# and then saves the content to the file.



myfile = raw_input("What is the name of your file? ")
mywriting = raw_input("What would you like to add to the file? ")
myfile = open(myfile, 'w')
myfile.write(mywriting)

myfile.close()
