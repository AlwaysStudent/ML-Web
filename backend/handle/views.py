from django import http
import pandas as pd
import base64

import common


def handle_init(request):
    request_dict = common.handle_request(request)
    filename = request_dict['data'] + '_' + request_dict['dataset'] + '.csv'
    file_df = pd.read_csv('./public/1/' + filename).head(100)
    header_list = list(file_df.columns)
    response_table_label = []
    for i in header_list:
        response_table_label.append(
            {
                'prop': i,
                'label': i
            }
        )
    response_table_data = []
    for index, row in file_df.iterrows():
        response_table_data.append(row.to_json())
    return http.JsonResponse(
        {
            'tableLabel': response_table_label,
            'tableData': response_table_data
        }
    )


def handle_pre(request):
    request_dict = common.handle_request(request)
    filename = request_dict['data'] + '_Train.csv'
    file_df = pd.read_csv('./public/2/' + filename).head(100)
    header_list = list(file_df.columns)
    response_table_label = []
    for i in header_list:
        response_table_label.append(
            {
                'prop': i,
                'label': i
            }
        )
    response_table_data = []
    for index, row in file_df.iterrows():
        response_table_data.append(row.to_json())
    return http.JsonResponse(
        {
            'tableLabel': response_table_label,
            'tableData': response_table_data
        }
    )


def handle_select(request):
    request_dict = common.handle_request(request)
    filename = request_dict['data'] + '.csv'
    file_df = pd.read_csv('./public/3/' + filename).head(100)
    header_list = list(file_df.columns)
    response_table_label = []
    for i in header_list:
        response_table_label.append(
            {
                'prop': i,
                'label': i
            }
        )
    response_table_data = []
    for index, row in file_df.iterrows():
        response_table_data.append(row.to_json())
    return http.JsonResponse(
        {
            'tableLabel': response_table_label,
            'tableData': response_table_data
        }
    )


def handle_select_picture(request):
    request_dict = common.handle_request(request)
    filename = request_dict['data'] + '.png'
    with open('./public/3/' + filename, 'rb') as f:
        return http.HttpResponse(base64.b64encode(f.read()), content_type='image/png')
