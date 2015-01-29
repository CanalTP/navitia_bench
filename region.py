from stop_areas import StopAreas
from places import Places
from journeys import Journeys
from datetime import datetime


class Region:
    def __init__(self, server, id_, start_production, end_production):
        self.id_ = id_
        self.start_production = datetime(int(start_production[:4]),
                int(start_production[4:6]), int(start_production[6:8]))
        self.end_production = datetime(int(end_production[:4]),
                int(end_production[4:6]), int(end_production[6:8]))
        self.stop_areas = StopAreas(server, self)
        self.places = Places(self.stop_areas)
        self.journeys = Journeys(self)
        self.server = server

    def query(self, q):
        return self.server.query('v1/coverage/{}/{}'.format(self.id_, q))
