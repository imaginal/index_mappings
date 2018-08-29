#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import json

mapptings = {
    "awardCriteria": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "bid_id": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "code": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "postalCode": {
        "analyzer": "postalcode",
        "include_in_all": True
    },
    "email": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "telephone": {
        "analyzer": "telephone",
        "include_in_all": True
    },
    "streetAddress": {
        "include_in_all": True
    },
    "locality": {
        "include_in_all": True,
    },
    "countryName\w*": {
        "include_in_all": True,
    },
    "identifier\.id": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "\w+ID": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "lotID": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "contractNumber": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "cancellationReason": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "kind": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "related\w+": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "procurementMethodType": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "documentType": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "\w+Type": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "status": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "type": {
        "analyzer": "whitespace_lower",
        "include_in_all": False,
    },
    "identifier\.active": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "owner": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "owner_token": {
        "analyzer": "whitespace_lower",
        "include_in_all": False,
        "index": "no"
    },
    "scheme": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "submissionMethod": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "edrpou": {
        "analyzer": "whitespace_lower",
        "include_in_all": True
    },
    "reasonType": {
        "analyzer": "whitespace_lower",
        "include_in_all": False
    },
    "date\w*": {
        "format": "dateOptionalTime",
        "include_in_all": False,
        "type": "date"
    },
    "\w+Date": {
        "format": "dateOptionalTime",
        "include_in_all": False,
        "type": "date"
    },
    "\w+Url": {
        "include_in_all": False,
        "index": "no"
    },
    "hash": {
        "include_in_all": False,
        "index": "no"
    },
    "\w+ocuments\.id": {
        "include_in_all": False,
        "index": "no"
    },
    "\w+ocuments\.language": {
        "include_in_all": False,
        "index": "no"
    },
    "\w+ocuments\.url": {
        "include_in_all": False,
        "index": "no"
    },
    "\w+Comment": {
        "include_in_all": True
    },
    "name\w*": {
        "include_in_all": True
    },
    "title\w*": {
        "include_in_all": True
    },
    "description\w*": {
        "include_in_all": True
    },
    "complaints\.id": {
        "include_in_all": False,
        "index": "no"
    },
    "contracts\.id": {
        "include_in_all": False,
        "index": "no"
    },
    "lots\.id": {
        "include_in_all": False,
        "index": "no",
    },
    "bids\.id": {
        "include_in_all": False,
        "index": "no"
    },
    "qualifications\.id": {
        "include_in_all": False,
        "index": "no"
    },
    "elevation": {
        "include_in_all": False,
        "index": "no"
    },
    "latitude": {
        "include_in_all": False,
        "index": "no"
    },
    "longitude": {
        "include_in_all": False,
        "index": "no"
    },
    "amount": {
      "type": "double"
    },
    "quantity": {
      "type": "double"
    },
}


def test_mapping(data, path=''):
    if isinstance(data, list):
        for item in data:
            test_mapping(item, path)

    elif isinstance(data, dict):
        if "properties" in data:
            for key in data["properties"].keys():
                test_mapping(data["properties"][key], path + '.' + key)
        elif "type" in data:
            mapptings_items = sorted(mapptings.items(), key=lambda x: x[0])
            for key, prop in mapptings_items:
                if re.search(key + '$', path):
                    for kp, vp in prop.items():
                        if data.get(kp, None) != vp:
                            print path, key
                            print "\t", kp, data.get(kp), "!=", vp
                            data[kp] = vp


def main():
    with open(sys.argv[1]) as fp:
        data = json.load(fp)
        root = data

    if "mappings" in data:
        data = data["mappings"]

    if len(data) == 1:
        key = data.keys()[0]
        data = data[key]

    test_mapping(data)

    with open(sys.argv[2], 'w') as fp:
        json.dump(root, fp, ensure_ascii=False, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()

