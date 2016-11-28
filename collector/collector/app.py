# -*- coding: utf-8 -*-

import falcon

from collector.restviews.default import Collector


api = falcon.API()

# epics
api.add_route('/', Collector())
