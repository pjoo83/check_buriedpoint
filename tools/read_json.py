import json


def parse_json_file(file_path1):
    # 打开JSON文件并加载数据
    with open(file_path1, 'r', encoding='utf-8') as file:
        data = json.load(file)

    required_content = []
    for i in range(len(data)):
        if data[i]['request']['body']['text']:
            required_content.append(data[i]['request']['body']['text'])

    return required_content

