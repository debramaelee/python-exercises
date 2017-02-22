# nonsensical recursion method i found on google
#def triangle(i, t = 0):
#     if i == 0:
#         return 0
#     else:
#         print(' ' * (i + 1) + '*' * (t * 2 + 1))
#         return triangle(i - 1, t + 1)
#
# triangle(int((raw_input("Print a triangle "))))

#import sys -> sys.stdout (allow you to print multiple statement in one line)

rows = int(raw_input("How many rows in the pyramid? "))
col = (rows + 1) / 2
num_spaces = rows - 1
a = 1

for i in range(rows):
    stars = "*" * a
    x = " " * num_spaces
    print x + stars
    num_spaces -= 1
    a += 2

# alt solution
xr = 10

for x in range(0, xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print ' ' * spaces + '*' * stars
