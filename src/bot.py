import os, sys, signal, time, threading
import log, config

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# create LoadingString object & run its 'run' function in new thread
loading = log.LoadingString()
thread = threading.Thread(target = loading.run, daemon = True)
thread.start()

# check if configuration file exists
if not config.check_file('../config/config.ini'):
    loading.stop()
    time.sleep(1)
    config.create_config('../config/config.ini', log.start_time, log.log_length)
    sys.exit(0)

# load configuration from file & check its correctness
try:
    configuration = config.load_config('../config/config.ini')
except Exception as e:
    loading.stop()
    time.sleep(1)
    config.print_config_err(e, log.start_time, log.log_length)
    sys.exit(0)

# handle CTRL + C
def ctrl_c(signal, frame) -> None:
    log.print_log("", "", 2)
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

# stop LoadingString object loop
loading.stop()
time.sleep(1)

# write stdout to both console and file
sys.stdout = log.Logger()

# starting log message
log.print_log("", "", 1)

while True:
    pass