# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal
from json import JSONDecoder, JSONEncoder
import json

import logging


DEBUGGING = False

if DEBUGGING is True:
    logging.basicConfig()


class DateTimeDecoder(json.JSONDecoder):
    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                             *args, **kargs)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d


class DateTimeEncoder(JSONEncoder):
    """ Instead of letting the default encoder convert datetime to string,
        convert datetime objects into a dict, which can be decoded by the
        DateTimeDecoder
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
            """
            return {
                '__type__' : 'datetime',
                'year' : obj.year,
                'month' : obj.month,
                'day' : obj.day,
                'hour' : obj.hour,
                'minute' : obj.minute,
                'second' : obj.second,
                'microsecond' : obj.microsecond,
            }
            """
        elif isinstance(obj, Decimal):
            return int(obj.to_integral_value())
        else:
            return JSONEncoder.default(self, obj)
