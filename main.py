#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/12 17:35
# @Author  : tvhead98
# @File    : main.py

import pandas as pd
from get_geographic_info import *
from const import *
import json
import time

OUTPUT_FILE = 'output_data/geographic_info.data'

poi_list = pd.read_csv(POI_FILE)
poi_num = len(poi_list)

district_dict = {}
for p in range(poi_num):
    row = poi_list.loc[p]
    pos = str(row['lng']) + ',' + str(row['lat'])
    name = row['attraction']
    dis = get_poi_district(pos)
    district_dict[name] = dis
with open('district.data', mode='w', encoding='utf8') as f:
    for key in district_dict:
        f.write(key+'\t'+district_dict[key]+'\n')

# with open('raw_data/district.data', mode='r', encoding='utf8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         district_dict[line[0]] = line[1]

# print('fetching district done')
#
# f = open(OUTPUT_FILE, 'a', encoding='utf8')
#
# for o in range(79, poi_num):
#     for d in range(o+1, poi_num):
#         ori = poi_list.loc[o]
#         des = poi_list.loc[d]
#         ori_name = ori['attraction']
#         des_name = des['attraction']
#         ori_pos = str(ori['lng']) + ',' + str(ori['lat'])
#         des_pos = str(des['lng']) + ',' + str(des['lat'])
#         ori_district = district_dict[ori_name]
#         des_district = district_dict[des_name]
#         shortest_driving_time, taxi_fee_1 = get_shortest_driving_time(ori_pos, des_pos)
#         shortest_driving_path, taxi_fee_2 = get_shortest_driving_path(ori_pos, des_pos)
#         texi_fee = min(taxi_fee_1, taxi_fee_2)
#         data = {
#             'ori_name': ori_name,
#             'des_name': des_name,
#             'ori_district': ori_district,
#             'des_district': des_district,
#             'shortest_driving_time': shortest_driving_time,
#             'shortest_driving_path': shortest_driving_path,
#             'texi_fee': texi_fee
#         }
#         data = json.dumps(data, ensure_ascii=False)
#         f.write(data+'\n')
#         time.sleep(1)
#     print('{} pois done'.format(o+1))
#     time.sleep(1)
#
# f.close()
