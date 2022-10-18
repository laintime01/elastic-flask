from elasticsearch import Elasticsearch

import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
print(f"Connected to ElasticSearch cluster '{es.info()['cluster_name']}'")

with open("prog_book.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        bookList = {
            "Rating": line[0],
            "Reviews": line[1],
            "Book_title": line[2],
            "Description": line[3],
            "Page_Number": line[4],
            "Type": line[5],
            "price": line[6]
        }
        es.index(index="prog_books", doc_type="text" ,body=bookList)
