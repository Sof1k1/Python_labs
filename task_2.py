import csv
import json

def csv_to_json(filename: str):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = next(csv_reader)

        list_of_elements = []
        for row in csv_reader:
            dict_of_elements = {headers[i]: row[i] for i in range(len(headers))}
            list_of_elements.append(dict_of_elements)

    json_data = json.dumps(list_of_elements, indent=4)
    return json_data

print(csv_to_json("file.csv"))
