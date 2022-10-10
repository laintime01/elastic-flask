from elasticsearch import Elasticsearch


class elasticsearch():
    def __init__(self, index_name, index_type):
        self.es = Elasticsearch('http://localhost:9200')
        self.index_name = index_name
        self.index_type = index_type

    def search(self, query, count: int = 30):
        dict_1 = {
            "query": {
                "multi_match": {
                    "query": query,
                    "field": ["name", "year"]
                }
            }
        }
        match_data = self.es.search(index=self.index_name, doc_type=self.index_type, body=dict_1, size=count)
        return match_data
