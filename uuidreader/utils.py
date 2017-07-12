# -*- coding: utf-8 -*-
#!/usr/bin/env python

################################################################################
# MIT License - Share/modify/etc, but please keep this notice.
#
# Copyright (c) 2017 Peter Steensen, B.Sc
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

import uuid
import datetime


def debug_print(msg, debug=False):
    if debug:
        timestamp = '<%Y-%m-%d %H:%M:%S>'.format(datetime.datetime.now())
        print(timestamp + ' ' + msg)


def rfid_code_to_uuid(rfid_code, debug=False):
    '''
    Convert the RFID Code to a UUID in the format
    6ba7b810-9dad-11d1-80b4-00c04fd430c8

    :param rfid_code:
    :param debug:
    :return:
    '''

    debug_print('Convert RFID Code to UUID', debug)
    rfid_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(rfid_code)))
    debug_print(str(rfid_code) + ' -> ' + rfid_uuid, debug)
    return rfid_uuid

