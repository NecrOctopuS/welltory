import logging
import json
import jsonschema
import os

from jsonschema import SchemaError, ValidationError


logging.basicConfig(filename='app.log', filemode='w', format='%(process)d|%(levelname)s|%(message)s')
EVENTS_PATH = 'task_folder/event'
SCHEMAS_PATH = 'task_folder/schema'


def get_json_data_from_folder(path):
    data = []
    json_paths = os.listdir(path)
    for json_path in json_paths:
        full_path = os.path.join(path, json_path)
        with open(full_path) as json_file:
            data_from_file = json.load(json_file)
        if data_from_file:
            data.append({'path': full_path,
                         'json': data_from_file})
        else:
            logging.warning(f'{full_path} is not valid json.')
    return data


def validate_json(event, schema):
    try:
        jsonschema.validate(event['json'], schema['json'])
    except SchemaError as ex:
        logging.error(f"Schema {schema['path']} is not correct because {ex.message}")
    except ValidationError as ex:
        logging.error(f"Event {event['path']} not validated by {schema['path']} because {ex.message}.")


def main():
    events = get_json_data_from_folder(EVENTS_PATH)
    schemas = get_json_data_from_folder(SCHEMAS_PATH)
    for schema in schemas:
        for event in events:
            validate_json(event, schema)


if __name__ == '__main__':
    main()
