import os, sys, signal, time, threading
import requests
import log

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# create LoadingString object & run its 'run' function in new thread
loading = log.LoadingString()
thread = threading.Thread(target = loading.run, daemon = True)
thread.start()

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