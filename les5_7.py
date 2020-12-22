import os
import json

file_path = os.path.join(os.path.dirname(__file__), 'work7.txt')
file_path_json = os.path.join(os.path.dirname(__file__), 'work7.txt')

result = []
firms = {}
av_pr = {}

with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        data = line.split()
        firms[data[0]] = int(data[2]) - int(data[3])

profit = []
for value in firms.values():
    if value > 0:
        profit.append(value)

av_pr['average_profit'] = sum(profit) / len(profit)

result.append(firms)
result.append(av_pr)

with open(file_path, 'w', encoding='UTF-8') as file:
    json.dump(result, file)
