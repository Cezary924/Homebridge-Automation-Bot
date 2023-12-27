import json, os
import log, hb

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str) -> None:
    with open(path, 'w') as f:
        json.dump({"settings": {"ip": "XXX.XXX.XXX.XXX", "port": "XXXX", "username": "XXXXXX", "password": "XXXXXX"}}, f, indent = 4)
    log.print_log("A config file has been created successfully.", "Please, edit the configuration and run the script again.")

# save configuartion to file
def save_config(path: str, config_dict: dict) -> None:
    with open(path, 'w') as f:
        json.dump(config_dict, f, indent = 4)

# load configuartion from file
def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        loaded_config = json.load(f)
    if 'settings' not in loaded_config.keys():
        raise Exception("A 'settings' dict missing in config file.")
    for element in ['ip', 'port', 'username', 'password']:
        if element not in loaded_config['settings'].keys():
            raise Exception("A '" + element + "' missing in 'settings' dict in config file.")
    if 'accessories' not in loaded_config.keys():
        try:
            hb.get_access_token(loaded_config)
            accessories_layout = hb.get_accessories_layout()
            hidden_accessories = {}
            for room in accessories_layout:
                for service in room['services']:
                    if 'hidden' in service:
                        hidden_accessories["uniqueId"] = True
                    else:
                        hidden_accessories["uniqueId"] = False
            accessories = hb.get_accessories()
            for accessory in accessories:
                if accessory["uniqueId"] in hidden_accessories:
                    if hidden_accessories[accessory["uniqueId"]] == True:
                        del accessory
                        continue
                unwanted = set(accessory.keys()) - set(["uniqueId", "serviceName"])
                for unwanted_key in unwanted:
                    del accessory[unwanted_key]
            loaded_config['accessories'] = accessories
            save_config(path, loaded_config)
            log.print_log("A config file has been updated with accessories list.", "Please, edit the updated configuration and run the script again.")
        except Exception as e:
            raise Exception(str(e))
        raise Exception('')
    return loaded_config

# check correctness of loaded configuration
def check_correctness(configuration: dict) -> None:
    #TODO needs implementation
    #raise Exception
    pass

# print info about error during preparing configuration
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while loading the config file.", str(e))