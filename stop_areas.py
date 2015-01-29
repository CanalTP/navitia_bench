import math
import random

class StopAreas:
    def __init__(self, server, region):
        self.server = server
        self.region = region
        self.pagination = None

    def set_pagination(self):
        if self.pagination:
            return
        q = self.region.query('stop_areas')
        self.pagination = q.json()['pagination']
        total_result = self.pagination['total_result']
        items_per_page = self.pagination['items_per_page']
        self.pagination['nb_pages'] = int(math.ceil(total_result/items_per_page))


    def get_nb_pages(self):
        self.set_pagination()
        return self.pagination['nb_pages']

    def get_random(self):
        page = random.randrange(self.get_nb_pages())
        q = self.region.query('stop_areas?start_page={}'.format(page))
        j = q.json()
        items_on_page = j['pagination']['items_on_page']
        item = random.randrange(items_on_page)
        return j['stop_areas'][item]

