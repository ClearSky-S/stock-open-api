import ebest_util
import json

with open('users.txt', 'rt', encoding='UTF8') as file:
    contents = json.loads(file.read())
    ebest_util.printJSON(contents)
    print(contents["장준혁-모의투자"])