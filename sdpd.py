import sys
import re
from datetime import datetime

datetimes = []

regexp = r'(.*model time )(.*$)'

logfile = sys.argv[1]

with open(logfile) as f:
    for line in f:
        m = re.search(regexp, line)
        if m:
            datetimes.append(m.group(2))
        if 'total      ' in line:
            wallclock = float(line.split()[9])

timeformat = '%Y-%m-%d %H:%M:%S.000'
starttime = datetime.strptime(datetimes[0], timeformat)
endtime = datetime.strptime(datetimes[-1], timeformat)
duration = endtime - starttime

sdpd = duration.seconds / wallclock

print('Simulation start time:', starttime)
print('Simulation end time:  ', endtime)
print('Wall clock:', wallclock)
print('SDPD: ', sdpd)


