import json


DATA_SET = [
    'NSL_KDD',
    'UNSW_NB15'
]


def handle_request(request):
    request_data = request.body.decode('utf-8')
    request_dict = json.loads(request_data)
    return request_dict
