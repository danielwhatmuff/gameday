from __future__ import print_function

import json
import urllib
import boto3


s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    base = event['Records'][0]['s3']
    bucket = base['bucket']['name']
    key = urllib.unquote_plus(base['object']['key'].encode('utf8'))
    response = s3.get_object(Bucket=bucket, Key=key)
    body_string = response['Body'].read()
    body = json.loads(body_string)
    id = body['Id']
    num = body['PartNumber']
    data = body['Data']
    # does this object already exist in the destination?
    try:
        print("Found")
        exists_ = s3.get_object(Bucket='cob-db', Key='%s/%s' % (id, num))
    except Exception as e:
        s3.put_object(Bucket='cob-db', Key='%s/%s' % (id, num), Body=body_string)
    else:
        print("UGH DUPLICATE")
    return body_string
