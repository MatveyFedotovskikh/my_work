import json
now_date_day_month = '08.08'
with open(f'info_clients\json/09.08_info_client.json', encoding='utf-8') as f:
    json_students = json.load(f)
print(len(json_students.keys()))
