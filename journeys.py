from datetime import timedelta
import random

class Journeys:
    def __init__(self, region):
        self.region = region

    def get_random(self):
        from_ = self.region.places.get_random_id()
        to_ = self.region.places.get_random_id()
        while to_ == from_:
            to_ = self.region.places.get_random_id()
        p = random.randrange((self.region.end_production - self.region.start_production).days)
        hours = random.randrange(24)
        minutes = random.randrange(60)
        delta = timedelta(days=p, hours=hours, minutes=minutes)
        date = (self.region.start_production + delta).strftime('%Y%m%dT%H%M00')
        return self.get(from_, to_, date)

    def get(self, from_, to_, date):
        return self.region.query('journeys?from={}&to={}&datetime={}'.format(from_, to_, date))

