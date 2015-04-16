# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

now = None

def revlist(li):
    newli = []
    for i in li:
        newli.insert(0, i)
    return newli

def deep_reverse(arr):
    print 'reversin'
    fin = None
    finlist =[]

    if is_list(arr):
        fin = revlist(arr)
        print fin
        for i in fin:
            if is_list(i):
                nowrev = deep_reverse(i)
                finlist.append(nowrev)
            #    finlist.append(revlist(i))
            else:
                finlist.append(i)
        return finlist

    else:
        return arr





#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print "result of funct"
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
