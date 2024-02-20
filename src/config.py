import json, os

import log, hb

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str) -> None:
    with open(path, 'w') as f:
        json.dump({"settings": {"ip": "XXX.XXX.XXX.XXX", "port": "XXXX", "username": "XXXXXX", "password": "XXXXXX", "optional": {"latitude": "XX.XX", "longitude": "XX.XX"}}}, f, indent = 4)
    log.print_log("A config file has been created successfully.", "Please, edit the configuration and run the script again.")

# save configuartion to file
def save_config(path: str, config_dict: dict) -> None:
    with open(path, 'w') as f:
        json.dump(config_dict, f, indent = 4)

# load configuartion from file
def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        loaded_config = json.load(f)
    return loaded_config

# check correctness of loaded configuration
def check_correctness(configuration: dict, path: str) -> None:
    if 'settings' not in configuration.keys():
        raise Exception("A 'settings' dict missing in config file.")
    for element in ['ip', 'port', 'username', 'password']:
        if element not in configuration['settings'].keys():
            raise Exception("A key '" + element + "' missing in 'settings' dict in config file.")
    if 'accessories' not in configuration.keys():
        try:
            hb.get_access_token(configuration)
            accessories = hb.get_accessories()
            for accessory in accessories:
                if "values" not in accessory.keys():
                    del accessory
                    continue
                unwanted = set(accessory.keys()) - set(["uniqueId", "serviceName", "type"])
                characteristics = accessory['values'].keys()
                for unwanted_key in unwanted:
                    del accessory[unwanted_key]
                accessory['characteristics'] = []
                for value in characteristics:
                    accessory['characteristics'].append(value)
            configuration['accessories'] = accessories
            if 'automations' not in configuration.keys():
                configuration['automations'] = [{"uniqueId": "XXXXXXXX", "characteristic": "XXXXXXXX", "type": "timer", "data": {"period": "XXXX"}},{"uniqueId": "XXXXXXXX", "characteristic": "XXXXXXXX", "type": "scheduler", "data": {"startTime": "XX:XX", "stopTime": "XX:XX"}}]
            save_config(path, configuration)
            log.print_log("A config file has been updated with accessories list.", "Please, edit the 'automations' section of the updated configuration and run the script again.")
        except Exception as e:
            raise Exception(str(e))
        raise Exception('')
    for element in configuration["accessories"]:
        for element2 in ['type', 'serviceName', 'uniqueId', 'characteristics']:
            if element2 not in element.keys():
                raise Exception("A key '" + element2 + "' missing in a dict in 'accessories' list in config file.")
    if 'automations' not in configuration.keys() or ('automations' in configuration.keys() and len(configuration['automations']) == 0):
        if 'automations' not in configuration.keys():
            configuration['automations'] = [{"uniqueId": "XXXXXXXX", "characteristic": "XXXXXXXX", "type": "timer", "data": {"period": "XXXX"}},{"uniqueId": "XXXXXXXX", "characteristic": "XXXXXXXX", "type": "scheduler", "data": {"startTime": "XX:XX", "stopTime": "XX:XX"}}]
            save_config(path, configuration)
        log.print_log("A config file has no automations.", "Please, edit the 'automations' section of the configuration and run the script again.")
        raise Exception('')
    for element in configuration["automations"]:
        for element2 in ['type', 'data', 'uniqueId', 'characteristic']:
            if element2 not in element.keys():
                raise Exception("A key '" + element2 + "' missing in a dict in 'automations' list in config file.")

# print info about error during preparing configuration
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while loading the config file.", str(e))