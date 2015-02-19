from contextlib import contextmanager
import os
import random
import time
from server import Server


if os.environ.get('CONFIG_FILE'):
    conf = __import__(os.environ.get('CONFIG_FILE'))
else:
    import settings as conf


@contextmanager
def time_that(trans, timer_name):
    """
    measure time of all work done under the 'with'
    """
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    trans.custom_timers[timer_name] = elapsed_time


class Transaction(object):
    def __init__(self):
        self.api = Server(conf.URL, conf.TOKEN)

    def run(self):

        for r in self.api.regions.itervalues():
            with time_that(self, 'journeys_' + r.id_):
                res = r.journeys.get_random()

                assert res.status_code == 200

