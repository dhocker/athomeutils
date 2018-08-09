# coding: utf-8

# Test app_trace module functions
# Copyright © 2018  Dave Hocker (email: AtHomeX10@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the LICENSE file for more details.

from app_trace import print_trace, log_trace
import app_logger


def func1():
    func2()


def func2():
    raise NameError("Forced exception")


if __name__ == "__main__":

    app_logger.EnableEngineLogging()
    logger = app_logger.getAppLogger()

    try:
        func1()
    except Exception as ex:
        print_trace(ex=ex)
        log_trace(logger, ex=ex)

    app_logger.Shutdown()