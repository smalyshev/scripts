import os
import sys
import collections
import json
import compare
import send_requests
from urllib.parse import quote

servers = ['wdq5', 'wdq4', 'wdq3', 'wdq21', 'wdq22', 'wdq23', 'wdq9', 'wdq10', 'wdq6', 'wdq7', 'wdq8', 'wdq24', 'wdq25', 'wdq26']

"""
Compare item data for all servers
"""
QUERY = """
SELECT ?s ?p ?o WHERE {
  { 
    BIND(wd:%s as ?s)
    ?s ?p ?o . 
    # SKIP for stability
    FILTER(?p != wikibase:timestamp)
  }
  UNION {
    wd:%s ?pp ?s .
    FILTER( STRSTARTS(STR(?s), str(wds:Q)))
    ?s ?p ?o .
  }
} ORDER BY ?s ?p ?o
"""
QUERY2 = """
SELECT *
WHERE 
{
  %s ?p ?o
  FILTER(?p != wikibase:timestamp)
} ORDER BY ?p ?o
# %s
"""

for qid in sys.argv[1:]:
    print(qid)
    q = quote(QUERY % (qid, qid))
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
