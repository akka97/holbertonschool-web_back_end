#!/usr/bin/env python3
"""insert module"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new doc in a collection based on kwargs"""
    kwargs_el = {}
    for k, v in kwargs.items():
        kwargs_el[k] = v
    doc_id = mongo_collection.insert_one(kwargs_el).inserted_id
    return doc_id
