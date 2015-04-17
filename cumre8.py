# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def is_list(p):
    return isinstance(p, list)


def longest_repetition(arr):
    elem = None
    last = None
    thiscount = 0
    count = 0
    for i in arr:
        #print i
        if last:
            if i == last:
                thiscount = thiscount + 1
            else:
                if thiscount > count:
                    elem = last
                last = i

                thiscount = 1
        else:
            last = i

    return elem



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
