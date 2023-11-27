import json

numbers = [1, 2, 3, 4]
# numbers 라는 리스트를 json 포맷으로 변경
numbers_string = json.dumps(numbers)
print(numbers_string)


# json 형식의 문자열을 준비
value_string = '{"x" : 10, "y" : 20, "size" : 4.5}'
value = json.loads(value_string)
print(type(value))
print(value)


with open('zombie_data.json', 'r') as f:
    zombie_data_list = json.load(f)
    print(zombie_data_list)