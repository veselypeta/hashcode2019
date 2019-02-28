#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:42:24 2019

@author: aimeeredbond
"""

class Photo:
    def __init__(self, photo_id, orientation, no_tags, tags_list):
        self.photo_id = photo_id
        self.orientation = orientation
        self.no_tags = no_tags
        self.tags_list = tags_list
    
    def __str__(self):
        return "Photo with id = {}, orientation = {} and n_tags = {}".format(self.photo_id, self.orientation, self.no_tags)
        
        
    
    