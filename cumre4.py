# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.




def remove_tags(blah):
    if '<' in blah:
        first = blah.find('<')
        closer = blah.find('>')
        if first == 0:
            blah = blah[closer+1:]
            print blah
            return remove_tags(blah)
            #still need to recursively call here
        else:
            start = blah[:first]
            end = blah[closer+1:]
            blah = start +' ' + end
            return remove_tags(blah)
        print blah[closer:+1]
    else:
        return blah.split()

#print remove_tags('''<h1>Title</h1><p>This is a
#                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
