#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:31:27 2019

@author: aimeeredbond
"""

from parse import *
from Photo import *

photos = parseData("a_example.txt")

def sortByOrientation(photos):
    
    horizontals = [h for h in photos if h.orientation=='H']
    verticals = [v for v in photos if v.orientation=='V']
    return horizontals, verticals

horizontals, verticals = sortByOrientation(photos)

def sortList(verticals):
    verticals.sort(key=lambda x: x.no_tags)
    return verticals

def getHorizontals(horizontals):
    horizontals.sort(key=lambda x: x.no_tags)
    return horizontals
