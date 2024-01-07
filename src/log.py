import sys, os, io, datetime, threading

# get start date & time
start_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# int variable storing info how long should log lines be
log_length = 102

# sync for attributes
def synchronized_with_attr(lock_name: str):
    def decorator(method):
        def synced_method(self, *args, **kws):
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)
        return synced_method
    return decorator

# write and open log file 'name' located in 'path'
def log_file(name: str, path: str) -> io.TextIOWrapper:
    try:
        os.makedirs(os.path.dirname(path), exist_ok = True)
        x = open(path, 'a')
    except OSError:
        print("ERROR: Open error - Could not open the \'" + name + "\' file.")
    return x

# class for logging instances
class Logger(object):
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.terminal = sys.stdout
        self.log = log_file("log_" + start_time + ".log", "../log/log_" + start_time + ".log")
    
    @synchronized_with_attr('lock')
    def write(self, message: str) -> None:
        self.terminal.write(message)
        self.log.write(message)
    
    def flush(self) -> None:
        pass

# print info about Bot's tasks
def print_log(info: str, info2: str = "", start_stop: int = 0, ver: str = "") -> None:
    if start_stop == 1:
        print("|" + "=" * (log_length - 2) + "|")
        print("|" + "+" * (log_length - 2) + "|")
        print("Homebridge Automation Bot".center(log_length, ' '))
        print(("v" + ver).center(log_length, ' '))
        print("by Cezary924".center(log_length, ' '))
        print("|" + "+" * (log_length - 2) + "|")
        print("|" + "=" * (log_length - 2) + "|")
        print(str(datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")))
        print(" " + "-" * (log_length - 2) + " ")
        print(" " + "The Bot has been started." + " ")
        print("|" + "=" * (log_length - 2) + "|")
        return
    if start_stop == -1:
        print(str(datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")))
        print(" " + "-" * (log_length - 2) + " ")
        print(" " + "The Bot has been stopped." + " ")
        print("|" + "=" * (log_length - 2) + "|")
        print("|" + "+" * (log_length - 2) + "|")
        print("Goodbye!".center(log_length, ' '))
        print("|" + "+" * (log_length - 2) + "|")
        print("|" + "=" * (log_length - 2) + "|")
        return
    print(str(datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")))
    print(" " + "-" * (log_length - 2) + " ")
    print(" " + info + " ")
    if len(info2) > 0:
        if info2.isascii():
            print(" - '" + info2 + "' ")
    print("|" + "=" * (log_length - 2) + "|")