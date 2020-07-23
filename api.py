import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"]=True


data = [
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5006", "type": "Chocolate with Sprinkles" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]



@app.route('/', methods=['GET'])

def home():
    return '<h1>Hello Flask app</h1><p>Welcome to Flask app</p>'


@app.route('/api/v1/getall', methods=['GET'])

def getDetails():
    return jsonify(data)

@app.route('/api/v1/detail', methods=['GET'] )

def get_detail():
    args = request.args
    results = []
    if 'id' in args:
        id = args['id']
        fil = list(filter(lambda x : x['id']==id, data))
        if len(fil)>0:
            results.append(fil)
        else:
            return "Id not found"
        print(jsonify(id))
    else:
        results = data
    return jsonify(results)

if __name__ == '__main__':
    app.run()