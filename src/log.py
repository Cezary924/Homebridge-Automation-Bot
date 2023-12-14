import sys, io, time, datetime, threading

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
        x = open(path, 'a')
    except OSError:
        print("ERROR: Open error - Could not open the \'" + name + ".txt\' file.")
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

# class defining LoadingString objects
class LoadingString():
    def __init__(self) -> None:
        self._dots = 0
        self._stop = False
        print('|' + 'Loading'.center(log_length - 2, ' ') + '|', end = '\r')
    def __str__(self) -> str:
        if self._dots >= 4:
            self._dots = 0
        text = 'Loading'.center(log_length - 2, ' ')
        text_split = text.split('Loading')
        if self._dots > 0:
            text = '|' + text_split[0] + 'Loading' + '.' * self._dots + text_split[1][:-self._dots] + '|'
        else:
            text = '|' + text_split[0] + 'Loading' + text_split[1] + '|'
        self._dots = self._dots + 1
        return text
    def run(self) -> None:
        while self._stop == False:
            print(self, end = '\r')
            time.sleep(0.5)
    def stop(self) -> None:
        self._stop = True

# print info about Bot's tasks
def print_log(info: str, info2: str = "", start_stop: int = 0) -> None:
    if start_stop == 1:
        print('\r', end = '')
        print("|" + "=" * (log_length - 2) + "|")
        print("|" + "+" * (log_length - 2) + "|")
        print("Homebridge Automation Bot".center(log_length, ' '))
        print("by Cezary924".center(log_length, ' '))
        print("|" + "+" * (log_length - 2) + "|")
        print("|" + "=" * (log_length - 2) + "|")
        print(str(datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")))
        print(" " + "-" * (log_length - 2) + " ")
        print(" " + "The Bot has been started." + " ")
        print("|" + "=" * (log_length - 2) + "|")
        return
    if start_stop == 2:
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