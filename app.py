from flask import Flask, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
print(f"Connected to ElasticSearch cluster {es.info()['cluster_name']}")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_es')
def search_autocomplete():
    query = request.args['q']
    tokens = query.split(" ")
    print(tokens)
    return ""

if __name__ == '__main__':
    app.run(debug=True)
