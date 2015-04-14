# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(nonneg):
    if nonneg == 0:
        return '0'
	secs = nonneg%60
	secstr = 'seconds'
	nonneg = nonneg - secs
	finhour = ''
	finmin = ''
	if secs == 1:
		secstr = 'second'
	finsec = str(secs) + ' ' + secstr
	minstr = ' minutes'
	if nonneg/60. > 1 :

	    print 'more than a min'
	    print nonneg/60
        mins = nonneg/60.
        minfin = mins%60
        if minfin == 1:
            minstr = ' minute'
        mindiv = mins - minfin
        print mins
	finmin = str(int(minfin)) + ' ' + minstr
        if mins/60. > 1.0:
            hours = mindiv/60.
            hourst = ' hours'
            if hours == 1:
                hourst = ' hour'

            print 'more than an hour'
            hours = mins/60
            finhour = str(int(hours)) + hourst
            print hours
        else:
            finhour = '0 hours'
	return  finhour +', ' +finmin+ ', '  + finsec



print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds



print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

#passing 
def convert_seconds(nonneg):
        secs = nonneg%60
        secstr = 'seconds'
        nonneg = nonneg - secs
        finhour = ''
        finmin = ''
        if secs == 1:
                secstr = 'second'
        finsec = str(secs) + ' ' + secstr
        minstr = 'minutes'
        if nonneg/60. >= 1 :

            print 'more than a min'
            print nonneg/60
        mins = nonneg/60.
        minfin = mins%60
        if minfin == 1:
            minstr = 'minute'
        mindiv = mins - minfin
        print mins
        finmin = str(int(minfin)) + ' ' + minstr
        if mins/60. >= 1.0:
            hours = mindiv/60.
            hourst = ' hours'
            if hours == 1:
                hourst = ' hour'

            print 'more than an hour'
            hours = mins/60
            finhour = str(int(hours)) + hourst
            print hours
        else:
            finhour = '0 hours'
        return  finhour +', ' +finmin+ ', '  + finsec
