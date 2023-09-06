#!/usr/bin/env python3
"""List all doc inside a collection"""


def list_all(mongo_collection):
    """Func that list all doc inside a collect"""
    collection_list = []

    for data in mongo_collection.find():
        if data:
            collection_list.append(data)
    return collection_list
