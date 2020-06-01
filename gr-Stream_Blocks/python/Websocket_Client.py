#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-Stream_Blocks author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
import socket

class Websocket_Client(gr.sync_block):
    """
    docstring for block Websocket_Client
    """
    def __init__(self, address, portNumber):
        gr.sync_block.__init__(self,
            name="Websocket_Client",
            in_sig=[numpy.float32, ],
            out_sig=None)
        self.address=address
        self.port=portNumber
        self.socket=socket.socket()

        # Connect to the socket server
        self.socket.connect((self.address,self.port))
        print("Conenction to the socket server successful!")






    def work(self, input_items, output_items):
        
        in0 = input_items[0]
        # <+signal processing here+>
        for i in in0:
            self.socket.send(str(i).encode())
        return len(input_items[0])

