import json, os

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str, start_time: str, log_length: int) -> None:
    with open(path, 'w') as f:
        json.dump({"settings": {"ip": "XXX.XXX.XXX.XXX", "port": "XXXX", "login": "XXXXXX", "password": "XXXXXX"}}, f, indent = 4)
    print_config_info("A config file has been created successfully.", "Please, edit the configuration and run the script again.", start_time, log_length)

# load configuartion from file
def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        loaded_config = json.load(f)
    if 'settings' not in loaded_config.keys():
        pass
    all_elements_in_dict = all(element in loaded_config['settings'] for element in ['ip', 'port', 'login', 'password'])
    if not all_elements_in_dict:
        pass
    return loaded_config

# save configuartion to file
def save_config(path: str, config_dict: dict) -> None:
    with open(path, 'w') as f:
        json.dump(config_dict, f, indent = 4)

# print info about error during preparing configuration
def print_config_err(e: Exception, start_time: str, log_length: int, info: str = "") -> None:
    print_config_info("An error has occured while loading the config file.", str(e), start_time, log_length, info)