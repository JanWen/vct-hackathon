from chalice import Chalice
import uuid
import ml

app = Chalice(app_name='vct-backend')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route("/get_session_id", methods=['GET'])
def get_session_id():
    return str(uuid.uuid1())

@app.route('/converse', methods=['POST'])
def converse_new():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return ml.converse(user_as_json)

@app.route('/converse_agent', methods=['POST'])
def converse():
    # This is the JSON body the user sent in their POST request.
    json_body = app.current_request.json_body
    if "session_id" not in json_body:
        return {"error": "session_id field is required"}
    if "text" not in json_body:
        return {"error": "text field is required"}
    # We'll echo the json body back to the user in a 'user' key.
    return ml.converse_agent(json_body['session_id'], json_body['text'])
