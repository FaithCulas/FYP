#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-Stream_Blocks author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class SL_Matrix_Generator(gr.basic_block):
    """
    docstring for block SL_Matrix_Generator
    """
    def __init__(self, inVlen,windowSize,stride):
        gr.basic_block.__init__(self,
            name="SL_Matrix_Generator",
            in_sig=[(numpy.complex64,inVlen), ],
            out_sig=[(numpy.complex64,inVlen*windowSize), ])

        #initialize attributes    
        self.buffer=[]
        self.inVlen=inVlen
        self.stride=stride
        self.windowSize=windowSize

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            if len(self.buffer)==0:
                ninput_items_required[i] = self.windowSize + self.stride * (noutput_items-1)
            else:
                ninput_items_required[i] = self.stride * noutput_items


    def general_work(self, input_items, output_items):
        in0=numpy.array(input_items[0])
        output_items[0]=numpy.array(output_items[0])

        #Reshape the output buffer as an array of windows
        output_items[0]=output_items[0].reshape(len(output_items[0]),self.windowSize,self.inVlen)

        print("=======================================================")
        print("------------------GENERAL WORK FUNCTION ---------------")
        
        if len(self.buffer)==0:
            print("****INITIAL STATE: buffer empty")
            
            print("Input shape",in0.shape)
            print("output shape:",len(output_items[0]))

            #putting sliding windows in the output buffer
            for i in range(len(output_items[0])):
                start=self.stride*i
                output_items[0][i]=in0[start:start+self.windowSize]

            print("LAST WINDOW:......")
            print(output_items[0][-1])
            
            #Set buffer for the next general_work iteration
            self.buffer=numpy.copy(output_items[0][-1][self.stride:])
            self.buffer=numpy.array(self.buffer)
            print("[INFO] buffer set...")
            print("[INFO] buffer shape",self.buffer.shape)
            print("CURRENT BUFFER: ")
            print(self.buffer)

            # Consume the PROCESSED No of inputs
            self.consume(0, self.windowSize + self.stride * (len(output_items[0]-1)))
            print("****INITIAL STATE: COMPLETED")
        else:
            print("++++++++BUFFER NOT EMPTY++++++")
            copyOfin0=numpy.copy(in0)
            print("input len before buffer:",len(copyOfin0))
            print("copyOfin0 shape:",copyOfin0.shape)
            print("buffer shape: ",self.buffer.shape)

            #Merge the buffer and the input vector stream
            copyOfin0=numpy.concatenate((self.buffer, copyOfin0))

            print("input len after appending buffer:",len(copyOfin0))

            #putting sliding windows in the output buffer
            for i in range(len(output_items[0])):
                start=self.stride*i
                output_items[0][i]=copyOfin0[start:start+self.windowSize]

            print("FIRST WINDOW:.....")
            print(output_items[0][0])
            print("LAST WINDOW:.....")
            print(output_items[0][-1])

            #Set buffer for the next general_work iteration
            self.buffer=numpy.copy(output_items[0][-1][self.stride:])
            self.buffer=numpy.array(self.buffer)
            
            #Consume the PROCESSED No of inputs
            self.consume(0, self.stride*len(output_items[0]))

        return len(output_items[0])
