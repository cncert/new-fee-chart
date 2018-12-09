# encoding: utf-8
# 获取营业厅数据并转换为地图数据
import requests
import json
from collections import defaultdict
import time

GEOJSON_FILE = 'mobile_data.geojson'
final_list = []
features_list = []


def gaode_chinaarea(name, page):
    ''' 获取高德的中国行政区
    文档地址: http://lbs.amap.com/api/webservice/reference/district/#t5

    lat：纬度
    lng：经度
    '''
    gaode_url = 'https://restapi.amap.com/v3/place/text'
    requests_params = {
        'keywords': name,
        'city': 'beijing',
        'children': 1,
        'offset': 20,
        'extensions': 'all',
        'page': page,
        'key': 'f2cc6053971c5c73ae097f96e62c321e',
    }

    # gaode_url = 'http://restapi.amap.com/v3/config/district'
    # requests_params = {
    #     'keywords': '中华人民共和国',
    #     'level': 'country',
    #     'subdistrict': 3,
    #     'extensions': 'base',
    #     'key': 'f2cc6053971c5c73ae097f96e62c321e',
    # }

    print('Get Gaode data from {}{}'.format(gaode_url, page))
    response = requests.get(url=gaode_url, params=requests_params)

    if response.status_code == requests.codes.ok:
        print(response.json())
        return response.json()
    else:
        print('ERROR: Get Gaode data error')
        exit(1)


def generate_feature_data(map_data):
    location = map_data['location'].split(',')
    feature_data = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": location
        },
        "properties": {
            'id': map_data['id'],
            "gaode_map_id": map_data['id'],
            "name": map_data['name'],
            "province": map_data['pname'],
            "city": map_data["cityname"],
            "district": map_data["adname"],
            "address": map_data["address"],
            "phone": map_data["tel"] or '',
        },
    }
    return feature_data


def genete_feature_list(name, page):
    map_datas = gaode_chinaarea(name=name, page=page)
    map_datas = map_datas['pois']
    for map_data in map_datas:
        feature_data = generate_feature_data(map_data)
        features_list.append(feature_data)


def generate_geojson():
    geojson_data = {
        "type": "FeatureCollection",
        "features": features_list,
    }
    return geojson_data


def main():
    flag = -1
    for page in range(1, 900):
        time.sleep(0.2)
        genete_feature_list(name='移动营业厅', page=page)
        print(len(features_list))
        if flag != len(features_list):
            flag = len(features_list)
        else:
            break
    for page in range(1, 900):
        time.sleep(0.2)
        genete_feature_list(name='联通营业厅', page=page)
        print(len(features_list))
        if flag != len(features_list):
            flag = len(features_list)
        else:
            break
    for page in range(1, 900):
        time.sleep(0.2)
        genete_feature_list(name='电信营业厅', page=page)
        print(len(features_list))
        if flag != len(features_list):
            flag = len(features_list)
        else:
            break
    geojson_data = generate_geojson()
    with open(GEOJSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(geojson_data, f, ensure_ascii=False)
        print("Write file {} done".format(GEOJSON_FILE))


if __name__ == '__main__':
    main()