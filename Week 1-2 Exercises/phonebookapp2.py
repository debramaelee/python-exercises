import pickle

phone_entries = {'Debra': '111111'}



print
"""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save to file
6. Load from file
7. Quit


"""
While True:
    user_input0 = int(raw_input("What do you want to do (1-7)? "))
#If they choose to look up an entry, you will ask them for the person's name,
#and then look up the person's phone number by the given name and print it to the screen.
        if user_input0 == 1:
            user_input1 = raw_input("What is the person's name? ")
            phone = phone_entries.get(name, 'not listed')
            print "%'s number is %s" % (name, phone)
        elif user_input0 == 2:
            name = raw_input('Name? ')
            phone = raw_input('Phone Number? ')
            phone_entries[name] = phone
        elif user_input0 == 3:
            name = raw_input('Name? ')
            del phone_entries[name]
        elif user_input0 == 4:
            #to print phone book in a nice looking way
            for entry in phone_entries.items():
                print "%s's number is %s" % entry
        elif user_input0 == 5:
            my_file = open('phonebookapp.pickle', 'w')
            pickle.dump(phone_entries, my_file)
            my_file.close()
            print 'Saved'
            break
        elif user_input0 == 6:
            my_file = open('phonebookapp.pickle', 'r')
            #
            phone_entries = pickle.load(my_file)
            my_file.close()
            print "Restored phonebook"
        elif user_input0 == 7:
            break






#     if user_input1 in phone_entries:
#         print "Found entry for", user_input1, [phone_entries][user_input1]['Phone Number']
#     if user_input1 not in phone_entries:
#         print "User not found"
#
# # If they choose to set an entry, you will prompt them for the
# # person's name and the person's phone number
# if user_input0 == "2":
#     user_input2_name = raw_input("Name? ")
#     user_input2_num = raw_input("Number? ")
#     if user_input2_name not in phone_entries:
#         phone_entries[user_input2_name].append(1)
#         #doesnt work
#         #user_input2_name = append[1]["Name"]
#         #user_input2_num = append[1]["Number"]
#         print "Entry stored for", user_input2_name
#     if user_input2_name in phone_entries:
#         print "Name already exists."
#
# # If they choose to delete an entry, you will prompt them for the person's
# # name and delete the given person's entry.
# if user_input0 == "3":


# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# If they choose to quit, end the program.
