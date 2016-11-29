from __future__ import print_function

import json
import urllib
import boto3
import urllib2


s3 = boto3.client('s3')
API_BASE = 'https://dashboard.cash4code.net/score'
API_token = '22120b5ee1'


def lambda_handler(event, context):
    base = event['Records'][0]['s3']
    bucket = base['bucket']['name']
    key = urllib.unquote_plus(base['object']['key'].encode('utf8'))
    id, num = key.split('/')
    response = s3.get_object(Bucket=bucket, Key=key)
    other_num = '0' if num == '1' else '1'
    other_key = '%s/%s' % (id, other_num)
    result = 'good'
    try:
        other_response = s3.get_object(Bucket=bucket, Key=other_key)
        body_string = response['Body'].read()
        body = json.loads(body_string)
        other_body_string = other_response['Body'].read()
        other_body = json.loads(other_body_string)
        id = body['Id']
        num = body['PartNumber']
        data = body['Data']
        if num == 0:
            to_send = data + other_body['Data']
        else:
            to_send = other_body['Data'] + data
        url = API_BASE + '/' + id
        req = urllib2.Request(url, data=to_send, headers={'x-gameday-token':API_token})
        resp = urllib2.urlopen(req)
        resp.close()
    except Exception:
        print('Other key "%s" not found' % other_key)
        result = 'bad'
    return result
