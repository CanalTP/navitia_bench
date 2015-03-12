import requests
from region import Region


class Server:
    def __init__(self, host, token):
        self.host = host if host[:7] == "http" else "http://{}".format(host)
        self.token = token
        self.regions = {}
        self.set_regions()

    def query(self, url):
        full_url = "{}/{}".format(self.host, url)
        return requests.get(full_url, auth=(self.token, ''))

    def set_regions(self):
        if not self.regions:
            r = self.query('v1/coverage')
            for region in r.json()['regions']:
                r_id = region['id']

                if region['status'] != 'running':
                    print "region {} is not running, skipping it".format(r_id)
                    continue

                self.regions[r_id] = Region(self, r_id,
                                            region['start_production_date'],
                                            region['end_production_date'])
                print "region {} is has been set".format(r_id)
