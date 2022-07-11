import json, os
from flask import Flask, Response, request
import boto3
from boto3.dynamodb.conditions import Key
import urllib, urllib.request


instance_id = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
dynamo_table_name = os.environ.get('TC_DYNAMO_TABLE','Candidates')
dyndb_client = boto3.resource('dynamodb', region_name='us-east-2')
dyndb_table = dyndb_client.Table('Candidates')

candidates_app = Flask(__name__)

@candidates_app.route('/', methods=['GET'])
def default():
    return {"status": "invalid request"}, 400

@candidates_app.route('/gtg', methods=['GET'])
def gtg():
    details = request.args.get("details")

    if ("details" in request.args):
        return {"connected": "true", "instance-id": instance_id}, 200
    else:
        return Response(status = 200)

@candidates_app.route('/candidate/<name>', methods=['GET'])
def get_candidate(name):
    try:
        response = dyndb_table.query(
            KeyConditionExpression=Key('CandidateName').eq(name)
        )

        if len(response['Items']) == 0:
            raise Exception

        print(response['Items'])
        return json.dumps(response['Items']), 200

    except:
        return "Not Found", 404

@candidates_app.route('/candidate/<name>', methods=['POST'])
def post_candidate(name):
    try:
        response = dyndb_table.put_item(Item={"CandidateName": name})
    except Exception as ex:
        return "Unable to update", 500

    return {"CandidateName": name}, 200

@candidates_app.route('/candidates', methods=['GET'])
def get_candidates():
      try:
        items = dyndb_table.scan()['Items']

        if len(items) == 0:
            raise Exception

        return json.dumps(items), 200

      except:
        return "Not Found", 404


