#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio STREAM_BLOCKS module. Place your Python package
description here (python/__init__.py).
'''
from __future__ import unicode_literals

# import swig generated symbols into the Stream_Blocks namespace
try:
    # this might fail if the module is python-only
    from .Stream_Blocks_swig import *
except ImportError:
    pass

# import any pure python here
from .SL_Matrix_Generator import SL_Matrix_Generator
from .Websocket_Client import Websocket_Client
#
