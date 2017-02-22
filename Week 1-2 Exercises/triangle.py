col = 7
num_spaces = int(col / 2)
a = 1


for i in range(4):
    stars = "*" * a
    x = " " * num_spaces
    print x + stars
    num_spaces -= 1
    a += 2



    # if i == 1:
    #     num_spaces -= 1
    #     a += 2
    #     stars = "*" * a
    #     x = " " * num_spaces
    #     print x + stars + x
    # if i == 2:
    #     num_spaces -= 1
    #     a += 2
    #     stars = "*" * a
    #     x = " " * num_spaces
    #     print x + stars + x
    # if i == 3:
    #     num_spaces -= 1
    #     a += 2
    #     stars = "*" * a
    #     x = " " * num_spaces
    #     print x + stars + x



    #
    #     print "  " + "*" + "  "
    # elif i == 1:
    #     star_num = "*" * (i + 2)
    #     print " " + star_num + " "
    # else:
    #     star_num = "*" * (i + 3)
    #     print star_num
