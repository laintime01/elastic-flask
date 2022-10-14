from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
print(f"Connected to ElasticSearch cluster {es.info()['cluster_name']}")
CORS(app, resource={r"/*": {'origins': "*"}})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_es', methods=['POST'])
def search_autocomplete():
    post_data = request.get_json()
    print(post_data)
    val = post_data.get('input')
    obj_response = {'message': 'success'}
    constant_query = {
        "query": {
            "constant_score": {
                "filter": {
                    "term": {
                        "name": val
                    }
                }
            }
        }
    }
    query_body = {
        "query": {
            "match": {
                "name": val
            }
        }
    }
    obj_response['infos'] = es.search(index="cars", body=query_body)
    return jsonify(obj_response)


@app.route('/analyze', methods=['GET'])
def analyze_data():
    print("analyze")
    query_body = {
        "query": {
            "match": {
                "name": "bmw"
            }
        },
        "aggs": {
            "all_years": {
                "terms": {
                    "field": "name"
                }
            }
        }
    }
    return es.search(index="cars", body=query_body)

if __name__ == '__main__':
    app.run(debug=True)
