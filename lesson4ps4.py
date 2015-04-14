# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def download_time(fisi, fiun, band, baun):
    fibits = getbits(fisi,fiun)
    bandbi = getbits(band,baun)
    seconds = (fibits*1.0)/bandbi
    ender = ''
    if seconds > 60:
        #stuff to do if more than a min
        ender = 'gotta do some work ' + str(seconds)
    else:
        ender = '0 hours, 0 minutes, ' + str(seconds) + 'seconds'
    return convert_seconds(seconds)

def getbits(fisi, fiun):
    	bits = fisi
    	if fiun == 'kB':
    		bits = 2**10 *8* fisi
    	elif fiun == 'kb':
    		bits = 2**10 * fisi
    	elif fiun == 'Mb':
    		bits = 2** 20 * fisi
    	elif fiun == 'MB':
    		bits = 2**20 * 8 * fisi
    	elif fiun == 'Gb':
    		bits = (2 ** 30. )* fisi
    	elif fiun == 'GB':
    		bits = (2. ** 30 )* fisi
    	elif fiun == 'Tb':
    		bits = 2 ** 40 * fisi
    	elif fiun == 'TB':
    		bits = 2 **40 * 8 * fisi
        print 'bits are'
        print bits


    	return bits


def convert_seconds(nonneg):
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


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
