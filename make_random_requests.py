from server import Server
from stop_areas import StopAreas
import os, csv
from datetime import datetime

if os.environ.get('CONFIG_FILE'):
    conf = __import__(os.environ.get('CONFIG_FILE'))
else:
    import settings as conf

s = Server(conf.URL, conf.TOKEN)

for region in s.regions.itervalues():
    path = os.path.join(conf.BASE_DIR, "benchmarks", str(region))
    if not os.path.exists(path):
        os.execv("/bin/mkdir", ["-p", path])
    fname = "source_{}.csv".format(datetime.now().strftime("%x_%X"))
    with open(os.path.join(path, fname, 'wb')) as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in xrange(conf.NB_REQUESTS_PER_REGION):
            writer.writerow(region.journeys.make_random_request())
    result_file = os.path.join(path, "journeys.jtl")
    l = ["-n", "-t", conf.JMX_SCRIPT, "-Jjourneys_results",
        result_file, "-Jjourneys_dataset", fname, "-Jserver_url",
        conf.URL, "-Jserver_port", conf.PORT, "-Jserver_key", conf.TOKEN,
        "-Jregion_name", str(region)]
    print l
    os.execv("/usr/bin/jmeter", l)

