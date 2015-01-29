from stop_areas import StopAreas
import random
import math

def move_lat_long(latitude, longitude, distance, bearing):
        bearing = convert_to_radians(bearing)
        latitude = convert_to_radians(latitude)
        longitude = convert_to_radians(longitude)
        # earths radius in kilometers
        earth_radius = 6371
        d = float(distance)/float(earth_radius)
        latitude2 = math.asin( math.sin(latitude) * math.cos(d) + math.cos(latitude) * math.sin(d) * math.cos(bearing) )
        longitude2 = longitude + math.atan2( math.sin(bearing) * math.sin(d) * math.cos(latitude), math.cos(d) - math.sin(latitude) * math.sin(latitude2) )
        return convert_to_degrees(latitude2), convert_to_degrees(longitude2)

def convert_to_degrees(number):
        return (float(number) * (180/math.pi))

def convert_to_radians(number):
        return (float(number) * (math.pi/180))


class Places:
    def __init__(self, stop_areas):
        self.stop_areas = stop_areas

    def get_random_id(self):
        t = random.randrange(3)
        s = self.stop_areas.get_random()
        if t == 0:
            return s['id']
        elif t == 1:
            while not 'administrative_regions' in s:
                s = self.stop_areas.get_random()
            return s['administrative_regions'][0]['id']
        elif t == 2:
            distance = random.randrange(500)/1000
            bearing = random.randrange(360)
            new_p = move_lat_long(s['coord']['lat'], s['coord']['lon'], distance,
                    bearing)
            return "{};{}".format(new_p[1], new_p[0])

