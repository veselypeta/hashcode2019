#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:42:24 2019

@author: aimeeredbond
"""

def vocabulary(photos):
    vocabulary = []
    for photo in photos:
        for tag in photo.tags_list:
            if tag not in vocabulary:
                vocabulary.append(tag)
    return vocabulary

class Photo:
    def __init__(self, photo_id, orientation, no_tags, tags_list):
        self.photo_id = photo_id
        self.orientation = orientation
        self.no_tags = no_tags
        self.tags_list = tags_list
    
    def __str__(self):
        return "Photo with id = {}, orientation = {} and n_tags = {}".format(self.photo_id, self.orientation, self.no_tags)
    
    def vector(self, vocabulary):
        vector = [0] * len(vocabulary)
        for i, tag in enumerate(vocabulary):
            if tag in self.tags_list:
                vector[i] = 1
        return vector
        
    
    
