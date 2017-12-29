# -*- coding: UTF-8 -*-
import logging


def get_logger(file_name):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=file_name+'.log',
                        filemode='a')
    return logging
