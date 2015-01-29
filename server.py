import requests
from region import Region

class Server:
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.regions = {}
        self.set_regions()

    def query(self, url):
        full_url = "{}/{}".format(self.host, url)
        print full_url
        return requests.get(full_url, auth=(self.token, ''))

    def set_regions(self):
        if not self.regions:
            r = self.query('v1/coverage')
            for region in r.json()['regions']:
                self.regions[region['id']] = Region(self, region['id'],
                region['start_production_date'],
                region['end_production_date'])
