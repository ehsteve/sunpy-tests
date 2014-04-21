from sunpy.time import TimeRange
from sunpy.lightcurve import GOESLightCurve

dt = TimeRange('1981/01/10 00:00', '2014/04/18 23:00')

tr_not_found = []

time_ranges = dt.window(60*60*24, 60*60*24)
total_days = len(time_ranges)
total_fails = 0

# missing files http://umbra.nascom.nasa.gov/goes/fits/2005/go1220051116.fits
# http://umbra.nascom.nasa.gov/goes/fits/2005/go1220051116.fits
for time_range in time_ranges:
    print(time_range.start())
    try:
        goes = GOESLightCurve.create(time_range)
        print(goes.data['xrsa'].max())
        print(goes.data['xrsb'].max())
    except:
        print("File Not Found!")
        tr_not_found.append(time_range)
        total_fails = total_fails + 1

print('Number of fails:%i' % total_fails)
print('Number of tries:%i' % total_days)
print('Percent Fail: %d' % (float(total_fails)/total_days * 100))

for tr in tr_not_found:
    print(tr.start())