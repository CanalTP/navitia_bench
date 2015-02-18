from server import Server
from stop_areas import StopAreas
import os

if os.environ.get('CONFIG_FILE'):
    conf = __import__(os.environ.get('CONFIG_FILE'))
else:
    import settings as conf

s = Server(conf.URL, conf.TOKEN)

for region in s.regions.itervalues():
    for i in range(0, 100):
        print "success" if region.journeys.get_random().status_code == 200 else "failed"

