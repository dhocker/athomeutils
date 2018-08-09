# coding: utf-8
#
# app_trace - traceback utilities
# Copyright © 2018  Dave Hocker
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# See the LICENSE file for more details.
#

import traceback
import sys


def print_trace(ex=None):
    """
    Print traceback to stdout
    :return:
    """
    if ex:
        print("Exception:", type(ex))
        print(ex)
    else:
        print("Exception traceback")
    tb_str = traceback.format_tb(sys.exc_info()[2])
    for s in tb_str:
        # Trim trailing linefeed
        print(s[:len(s)-1])


def log_trace(logger, ex=None):
    """
    Log traceback to given logger instance
    :param logger: Where to log traceback.
    :return:
    """
    if ex:
        logger.error("Exception: %s", type(ex))
        logger.error(ex)
    else:
        logger.error("Exception traceback")
    tb_str = traceback.format_tb(sys.exc_info()[2])
    for s in tb_str:
        logger.error(s[:len(s)-1])
