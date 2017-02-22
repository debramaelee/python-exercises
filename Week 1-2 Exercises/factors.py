#student solution example
#
# user_num = int(raw_input("Enter a number "))
# last = user_num
# divisor = 1
#
# left = []
# right = []
#
# while (last > divisor):
#     if(user_num % divisor == 0):
#         last = user_num / divisor
#         if (last == divisor):
#             left.append(divisor)
#         else:
#             left.append(divisor)
#             right.insert(0, last)
#     divisor += 1
# print left + right

import math
n = int(raw_input("Enter a number "))

for i in range (1, math.sqrt(n)):
    if n % i == 0:
        little_bro = n/1
        big_bro = n / little_bro
        if little_bro == big_bro
            print little_bro
        else:
            print little_bro
            print big_bro

print "1"
