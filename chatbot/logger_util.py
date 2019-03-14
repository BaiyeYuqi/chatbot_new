# -*- coding: utf-8 -*-
import logging
import sys
import datetime


class MyFormatter(logging.Formatter):
    converter=datetime.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%b%d*%H:%M:%S")
            s = "%s" % t
        return s


def get_logger(level=logging.DEBUG, file_name=None):

    logger = logging.getLogger()  # root logger
    logger.setLevel(level)

    formatter = MyFormatter('*%(process)d %(asctime)s %(module)28s %(lineno)3d %(levelname)7s**   %(message)s')
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(level)
    logger.addHandler(stdout_handler)

    if file_name:
        file_handler = logging.FileHandler(filename=file_name)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    return logger
