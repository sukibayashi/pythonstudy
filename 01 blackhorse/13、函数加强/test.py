info = [{'id': '2', 'name': '楊', 'gender': '女'}, {'id': '1', 'name': '潘', 'gender': '男'}]

result = sorted(info, key=lambda x: (x['id']))
print(result)
print(info)
