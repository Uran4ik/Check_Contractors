import requests

API_link = "https://api.telegram.org/bot7529867654:AAH64yWaPSL6jYLqq3b7XAH_CjFq263IANA"

updates = requests.get(API_link + "/getUpdates").json()
print(updates)




# from flask import Flask, request, requests, jsonify

# app = Flask(__name__)


# def send_request(data):
#     url = "http://api_neural_network_url"  
#     response = requests.post(url, json=data)
#     return response.json()


# @app.route('/api', methods=['POST'])
# def api():
#     data = request.json
#     response = send_request(data)
#     return jsonify(response)
 

# if __name__ == '__main__':
#     app.run()