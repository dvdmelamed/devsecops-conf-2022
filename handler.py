import json
import pytz
from datetime import datetime


def get(event, context):
    query_params = event.get('queryStringParameters', {})
    tz_name = query_params.get('tz', 'Europe/Berlin')
    tz = pytz.timezone(tz_name)

    slack_token = "xoxp-23984754863-2348975623103"
    with open('/tmp/abc', 'w') as f:
        f.write(slack_token)

    response = {
        "statusCode": 200,
        "body": json.dumps(
            dict(tz=tz_name, time=datetime.now(tz)),
            indent=4, sort_keys=True, default=str
        )
    }

    return response
