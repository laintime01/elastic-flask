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
    obj_response = {'message': 'success'}
    post_data = request.get_json()
    print(post_data)
    query_body = {
        "query": {
            "match": {
                "name": "bmw"
            }
        }
    }
    obj_response['body'] = es.search(index="cars", body=query_body)
    return obj_response


if __name__ == '__main__':
    app.run(debug=True)
