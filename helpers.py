import json


def append_json(new_data, filename):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data.update(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

def start_json(data, filename):
        with open(filename, 'w+') as file:
                json_data = json.dumps(data)
                file.write(json_data)
                file.close()