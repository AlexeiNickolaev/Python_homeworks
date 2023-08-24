# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json

with open('data_base.json', 'r') as r:
    data = json.load(r)
    print(data)
    res_list = []
for key, values in data.items():
    for i in values:
        res_list.append({'level': key, 'id': i['id'], 'name': i['name']})


with open('res.csv', 'w') as res:
    temp = csv.DictWriter(res, fieldnames=['level', 'id', 'name'])
    temp.writerows(res_list)
