import sys
# i = 0
numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i += 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i

# print "The numbers: "

# for num in numbers:
#     print num


def add_number_and_print(count, count_plus):
    i = 0
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i += count_plus
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

add_number_and_print(7, 2)
for num in numbers:
    print num
