import json
import requests

api_url_base = 'http://ron-swanson-quotes.herokuapp.com/v2/'

headers = {'Content-Type': 'application/json'}

def get_quote():

    api_url = '{0}quotes'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        res = json.loads(response.content.decode('utf-8'))
        return ''.join(res)
    else:
        return None
