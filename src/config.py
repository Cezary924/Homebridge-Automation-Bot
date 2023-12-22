import json, os

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str, start_time: str, log_length: int) -> None:
    with open(path, 'w') as f:
        f.write('')
    line = "|" + "=" * (log_length - 2) + "|"
    text = line + "\n A config file has been created successfully.\n Please, edit the configuration and run the script again.\n" + line
    print('\r', end = '')
    print(text)
    with open('../log/log_' + start_time + '.log', 'w') as f:
        f.write(text)

# load configuartion from file
def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)

# save configuartion to file
def save_config(path: str, config_dict: dict) -> None:
    with open(path, 'w') as f:
        json.dump(config_dict, f)

# print info about loading configuration process
def print_config_info(info: str, info2: str, start_time: str, log_length: int, info3: str = ""):
    line = "|" + "=" * (log_length - 2) + "|"
    small_line = " " + "-" * (log_length - 2) + " "
    text = line + "\n " + info + "\n" + small_line + "\n - '" + info2 + "'\n"
    if info3 == "":
        text = text + line
    else:
        text = text + "\n - '" + info3 + "'\n" + line
    print('\r', end = '')
    print(text)
    with open('../log/log_' + start_time + '.log', 'w') as f:
        f.write(text)

# print info about error during preparing configuration
def print_config_err(e: Exception, start_time: str, log_length: int, info: str = ""):
    print_config_info("An error has occured while loading the config file.", str(e), start_time, log_length, info)