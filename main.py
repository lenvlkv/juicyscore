import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/get_token')
def hello_world():
    db_table_id = request.args.get('id')
    # TODO: read token from table==db_table_id and return token from there 
    output_token = 'TODO'
    return output_token


@app.route('/set_token', methods=['POST'])
def hello_post():
    input_data = request.json
    input_token = input_data['id']
    # input_token example is 'tok.qwerty123-456.A'
    split_res = input_token.split('.')
    db_table_id = split_res[2]
    # TODO: write token to the table db_table_id
    return 'Success'
