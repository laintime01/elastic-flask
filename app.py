from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch_class import ES

app = Flask(__name__)
car_es = ES(index_name="cars")
CORS(app, resource={r"/*": {'origins': "*"}})


@app.route('/')
def hello_world():  # put application's code here
    return 'ElasticSearch-Flask!'


@app.route('/get_es', methods=['POST'])
def search_autocomplete():
    post_data = request.get_json()
    print(post_data)
    val = post_data.get('input')
    obj_response = {'message': 'success'}
    query_body = {
        "query": {
            "match": {
                "name": val
            }
        }
    }
    obj_response['infos'] = car_es.search(query=query_body)
    return jsonify(obj_response)


@app.route('/books', methods=['POST'])
def get_books():
    post_data = request.get_json()
    print(post_data)
    val = post_data.get('input')
    book_es = ES(index_name="prog_books")
    query_book = {
        "query": {
            "match": {
                "Book_title": val
            }
        }
    }
    result = book_es.search(query=query_book)
    return result


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
    return car_es.search(query=query_body)


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="localhost")
