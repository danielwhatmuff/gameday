# -*- coding: utf-8 -*-

import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

try:
    app_env = os.environ['APP_ENV']
except KeyError:
    app_env = 'dev'

if app_env == 'dev':
    pass

elif app_env == 'stg':
    pass


elif app_env == 'prd':
    pass


elif app_env == 'lcl':
    # DB_SETTINGS['host'] = '127.0.0.1'
    pass
