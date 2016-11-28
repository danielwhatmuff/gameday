# -*- coding: utf-8 -*-

import json

from boto.s3.connection import S3Connection
from boto.s3.key import Key

from collector.constants import (STANDARD_OK_STATUS, COLLECTOR_BUCKET)
from collector.utils import DateTimeEncoder


class Collector(object):
    def on_post(self, req, resp, session=None, current_user=None, jwt_token=None):
        # get body as string:
        body =  req.stream.read().decode('utf8')
        # and the dict
        dict_val = json.loads(body)
        # write it to s3
        conn = S3Connection()
        k = Key(COLLECTOR_BUCKET)
        k.key = "%s/%s" % (dict_val['Id'], dict_val['PartNumber'])
        k.set_contents_from_string(body)
        resp.body = json.dumps({'results': body}, cls=DateTimeEncoder)
        resp.status = STANDARD_OK_STATUS
