import json

def sum_of_dict() -> float:
    with open('file.json', 'r') as file:
        data = json.load(file)
    sum_of_elements = 0.0
    for element in data:
        score = element.get("score", 0)
        weight = element.get("weight", 0)
        sum_of_elements += score * weight
    return round(sum_of_elements, 3)

print((sum_of_dict))
