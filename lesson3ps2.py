# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(mat):
	    # Your code her
	rowlen = len(mat)
	collen = len(mat[0])
	if rowlen != collen:
		return False
	row = 0
	for i in mat:
		print row
		col = 0
		


		for b in i:
			if b == mat[col][row]:
				print b
			else:
				return False

			col = col +1
	        row = row + 1
	return True

print symmetric([[1, 2, 3],
	       [2, 3, 4],
	       [3, 4, 1]])
	    #>>> Tru
print symmetric([["cat", "dog", "fish"],
	                    ["dog", "dog", "fish"],
	                    ["fish", "fish", "cat"]])
	    #>>> True

print symmetric([["cat", "dog", "fish"],
	                    ["dog", "dog", "dog"],
	                    ["fish","fish","cat"]])
	    #>>> False

	    #print symmetric([[1, 2],
	    #                [2, 1]])
	    #>>> True

	    #print symmetric([[1, 2, 3, 4],
	    #                [2, 3, 4, 5],
	    #                [3, 4, 5, 6]])
	    #>>> False

print symmetric([[1,2,3],
                [2,3,1]])
	    #>>> False
