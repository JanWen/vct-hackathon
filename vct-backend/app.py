from chalice import Chalice

import ml

app = Chalice(app_name='vct-backend')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/converse', methods=['POST'])
def converse():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return ml.converse(user_as_json['text'])

@app.route('/converse_new', methods=['POST'])
def converse_new():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return ml.converse_new(user_as_json)
