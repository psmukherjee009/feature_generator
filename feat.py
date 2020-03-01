#!/usr/bin/env python3

"""
Generates Derived data for single price data line. It keeps accumulating the data point to generate aggregate values
"""

Close_1 = ''
def atr(High, Low, Close):
    global Close_1
    if Close_1:
        catr = max([High - Low, abs(High - Close_1), abs(Close_1 - Low)])
        Close_1 = Close
        if catr:
            return catr
        return ''
    else:
        Close_1 = Close
    return ''
