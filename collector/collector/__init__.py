# -*- coding: utf-8 -*-


import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def test_lambda(*_, **__):
    logger.debug("Test lambda")
