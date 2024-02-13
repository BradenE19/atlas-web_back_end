#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
