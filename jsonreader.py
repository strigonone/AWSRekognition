import json


def json_parser():
    with open('AWSJsonData.json') as jsonData:
        data = json.load(jsonData)
        jsonData.close()
        varName = []
        for name in data['Labels']:
            varName.append(str(name['Name']).upper())
        # print(varName)
    return varName


