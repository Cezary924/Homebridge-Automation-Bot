import os, sys, signal, time, re

import log, config, database, automations, hb

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# write stdout to both console and file
sys.stdout = log.Logger()

# find current version number
version = "Error!"
try:
    with open('../SECURITY.md', 'r') as file:
        content = file.read()
        match = re.compile(r'\b\d+\.\d+\b').search(content)
        if match:
            version = match.group()
except Exception as e:
    pass

# starting log message
log.print_log("", "", 1, version)

# database variable
accessories_database = None

# handle exit (also with CTRL + C)
def ctrl_c(signal = None, frame = None) -> None:
    global accessories_database
    if accessories_database != None:
        del accessories_database
    log.print_log("", "", -1)
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

# check if configuration file exists
config_file_path = '../config/config.ini'
if not config.check_file(config_file_path):
    config.create_config(config_file_path)
    ctrl_c()

# load configuration from file & check its correctness
try:
    configuration = config.load_config(config_file_path)
    config.check_correctness(configuration, config_file_path)
except Exception as e:
    if str(e) != '':
        config.print_err(e)
    ctrl_c()

# get Homebridge API access token for the first time
try:
    hb.get_access_token(configuration)
except Exception as e:
    hb.print_err(e)
    ctrl_c()

# create Database object
try:
    accessories_database = database.Database(configuration['accessories'])
except Exception as e:
    hb.print_err(e)
    ctrl_c()

# get automations list from configuration
accessories_automations = configuration['automations']

# main script loop
timeout = 5
while True:
    time.sleep(timeout)
    try:
        hb.get_access_token(configuration)
        for automation in accessories_automations:
            accessories_database.update_accessory_value(automation['uniqueId'], automation['characteristic'])
            getattr(automations, automation['type'])(automation, accessories_database)
    except Exception as e:
        hb.print_err(e)
        continue