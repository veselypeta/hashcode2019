#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:31:27 2019

@author: aimeeredbond
"""

from parse import *

photos = parseData(filename)

def sortByOrientation(photos):
    
    horizontals = []
    verticals = []
    
    for photo in photos:
        if photo.orientation == 'H':
            horizontals.add(photo)
        else:
            verticals.add(photo)

