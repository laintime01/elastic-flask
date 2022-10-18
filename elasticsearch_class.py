from elasticsearch import Elasticsearch


class ES():
    def __init__(self, index_name):
        self.es = Elasticsearch('http://localhost:9200')
        self.index_name = index_name
        print(f"Connected to ElasticSearch cluster {self.es.info()['cluster_name']}")

    def search(self, query, count: int = 30):
        match_data = self.es.search(index=self.index_name, body=query, size=count)
        return match_data


