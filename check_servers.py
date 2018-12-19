import os
import sys
import collections
import json
import compare
import send_requests
from urllib.parse import quote

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

QUERY="""
SELECT ?item ?inv  WHERE {
  ?item p:P195 ?collectionstatement .
  ?collectionstatement ps:P195 wd:Q1068063 .
  ?item wdt:P31 wd:Q3305213 .
  ?item wdt:P217 ?inv . 
  } ORDER BY ?item
"""

args = sys.argv[1:]
if len(args) < 1:
    args = [None]
for qid in args:
    print(qid)
    q = quote( (QUERY % {'qid': qid})) )
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
