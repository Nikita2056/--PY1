import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as text:
        data = text.readline()
        data = [line.rstrip() for line in data]
    data_list = [val.split(",") for val in data]
    headers_list = data_list[0]
    list_dict = []
    for string in data_list[0]:
        dict_ = {headers_list[item]: string[item] for item in range(len(headers_list))}
        list_dict.append(dict_)

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
