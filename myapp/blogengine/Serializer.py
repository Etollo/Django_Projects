import json
import requests

data_serialize = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

json_string = json.dumps(data_serialize, indent=4)
print(json_string)

json_string_deserialize = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data_deserialize = json.loads(json_string_deserialize)
print(data_deserialize)

# response = requests.get('https://jsonplaceholder.typicode.com/todos/')
#
# todos = json.loads(response.text)
# print(type(todos))
# print(todos)