import os
TOKEN='da821360-5fdc-47cb-acc3-9025e56fd711'
URL='navitia2-ws.ctp.dev.canaltp.fr'
PORT='80'
BASE_DIR = '/var/lib/jenkins/jobs/bench_navitia_dev'
JMX_SCRIPT= os.path.join(BASE_DIR, 'benchmark.jmx')
NB_REQUESTS_PER_REGION=10
