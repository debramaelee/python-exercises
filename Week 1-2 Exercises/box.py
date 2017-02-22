
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for i in range(height):
    if i == 0 or i == height - 1:
        print "*" * width

    #if i < height - 1 and i > 0:
    else:
        num_blanks = width - 2
        print "*" + " " * num_blanks + "*"
