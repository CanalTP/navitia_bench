from server import Server
from stop_areas import StopAreas
import os, csv

if os.environ.get('CONFIG_FILE'):
    conf = __import__(os.environ.get('CONFIG_FILE'))
else:
    import settings as conf

s = Server(conf.URL, conf.TOKEN)

with open(conf.RESULT_FILE, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for region in s.regions.itervalues():
        for i in xrange(1000):
            writer.writerow(region.journeys.make_random_request())
