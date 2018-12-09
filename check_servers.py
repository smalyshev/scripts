import os
import sys
import collections
import json
import compare
import send_requests
from urllib.parse import quote

servers = ['wdq5', 'wdq4', 'wdq3', 'wdq21', 'wdq22', 'wdq23', 'wdq9', 'wdq10', 'wdq6', 'wdq7', 'wdq8', 'wdq24', 'wdq25', 'wdq26']

"""
Compare query results between different servers
"""
QUERY="""
SELECT ?item (count(?sense) as ?count) WHERE {
   ?l a ontolex:LexicalEntry ; dct:language ?item ; ontolex:sense ?sense .
} group by ?item order by desc(?count) ?item
"""

QUERY2="""
SELECT DISTINCT ?l WHERE {
   ?l a ontolex:LexicalEntry ; dct:language wd:%(qid)s ; ontolex:sense ?sense .
} order by ?l
# 
"""

args = sys.argv[1:]
if len(args) < 1:
    args = [None]
for qid in args:
    print(qid)
    q = quote( (QUERY % dict(qid=qid)) )
    results = collections.defaultdict(list)
    
    for res in send_requests.query_all(q):
        results[res[1]].append(res[0])

#    print(results)
    if len(results) > 1:
        for res in results:
#            print(res)
            # print(len(res))
            print(results[res])
            fname = ",".join(results[res])
            f = open(fname, 'w')
            f.write(res)
            f.close()
