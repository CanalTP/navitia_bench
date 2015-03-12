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
    print "Begin to benchmark {}".format(str(region))
    fname = "source_{}.csv".format(region)
    path = os.getcwd()
    source_fname = os.path.join(path, fname)
    print source_fname
    with open(source_fname, 'wb') as csvfile:
        with csv.writer(csvfile, delimiter=',') as writer:
            for i in xrange(conf.NB_REQUESTS_PER_REGION):
                writer.writerow(region.journeys.make_random_request())
    result_file = "journeys_{}.jtl".format(str(region))
    l = ["-n", "-t", conf.JMX_SCRIPT,
            "-Jjourneys_results", result_file, "-Jjourneys_dataset", source_fname,
            "-Jserver_url", conf.URL, "-Jserver_port", conf.PORT,
            "-Jserver_key", conf.TOKEN, "-Jregion_name", str(region)]
    os.system("sh {} {}".format(conf.JMETER_EXEC, " ".join(l)))
    print "Finished to benchmark {}".format(str(region))
