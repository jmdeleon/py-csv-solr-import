#!/usr/bin/python3

import sys, getopt
import csv, json
import pysolr

def main(args):
  inputfile='../csv/hello.csv'
  solr_url='http://localhost:8966/solr/py-csv-solr-import'

  # create connection to Solr server
  s = pysolr.Solr(solr_url, timeout=10)
  s.delete(q='*:*')

  # create records to submit to Solr
  record_count=0
  with open(inputfile) as f:
    reader = csv.reader(f)
    next(reader) # skip header line
    for splits in reader:
      record_count += 1
      # add record as JSON to Solr index
      s.add({
        "id":splits[0],
        "name":splits[1],
        "address":splits[2],
        "phone":splits[3],
        "age":splits[5],
        "join_date":splits[6]
        })

  s.commit()
  print('Done !!')

if __name__ == "__main__":
  main(sys.argv[1:])
