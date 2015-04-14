# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    print n
    onto = 1
    togo = []
    last = []
    while n >= onto:

        togo.append(makerow(last, onto))
        last = makerow(last, onto)
        print last

        onto = onto + 1

    return togo


def makerow(last, onto):
#    print last
    now = []
    if onto == 1:
        now = [1]
    else:
        if onto == 2:
            now = [1,1]
        elif onto == 3:
            now = [1,2,1]
        else:
            for i in range(onto):
#                print 'on pos'
#                print i
                if i == 0 or i == onto - 1:
                    now.append(1)
                else:
                    hey = last[i] +last[i-1]
                    now.append(hey)
#                    print 'last i'
                    #print last[i]


            print last
            print 'last above'


    return now



#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(9) #orig 6
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
