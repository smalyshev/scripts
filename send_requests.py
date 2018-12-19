import os
import subprocess
import sys
import collections
import json
import compare
from pebble import ThreadPool
import random

PRODUCTION = [ 'wdq5', 'wdq4', 'wdq6', 'wdq21', 'wdq22', 'wdq23' ] 
INTERNAL = [ 'wdq3', 'wdq7', 'wdq8', 'wdq24', 'wdq25', 'wdq26' ]
TEST = ['wdq9', 'wdq10']
SERVERS = PRODUCTION + INTERNAL + TEST
PROGRESS = True
DEBUG = False

def query(sparql, server, timeout=None):
    cmd = f"curl -s -XPOST localhost:9999/bigdata/namespace/wdq/sparql --data-binary 'query={sparql}' -H 'Accept: application/sparql-results+json'"
    try:
        with open(os.devnull, 'w') as devnull:
            res = subprocess.check_output(["ssh", server, cmd], shell = False, stderr = devnull, timeout=timeout)
    except subprocess.TimeoutExpired:
        if PROGRESS:
            print(server + " timed out!") 
        return []
    if DEBUG:
        print(res)
    try:
        data = json.loads(res.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        print(res)
        return []
    bindings = [x for x in data['results']['bindings'] if x != {}]
    if PROGRESS: 
        print(f"{server} Done") 
    return bindings
    
def query_server_data(sparql, server, parser):
    res = query(sparql, server)    
    return (server, parser(res))

def json_encode(res):
    return json.dumps(res, indent=2)

def query_all(sparql, data_parser=json_encode, servers=SERVERS):
    pool = ThreadPool(max_workers=10)
    results = collections.defaultdict(list)
    resmap = pool.map(lambda server: query_server_data(sparql, server, data_parser), servers)
    return resmap.result()

def random_server(servers=SERVERS):
    return random.choice(servers)