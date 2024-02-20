from datetime import datetime, timedelta
from suntime import Sun

import database, log

# check if device should be turned off
def timer(automation: dict, accessories_database: database.Database, settings: dict) -> None:
    if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 1:
        if accessories_database.get_accessory_date(automation['uniqueId']) + timedelta(seconds = int(automation['data']['period'])) < datetime.now():
            accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 0)
            log.print_log('Timer', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "'")

# check if device status is correct during specific schedule
def scheduler(automation: dict, accessories_database: database.Database, settings: dict) -> None:
    startTimeObj = None
    if automation['data']['startTime'] not in ['sunrise', 'sunset']:
        startTimeObj = datetime.strptime(automation['data']['startTime'], "%H:%M")
    else:
        try:
            sun = Sun(float(settings['optional']['latitude']), float(settings['optional']['longitude']))
        except Exception as e:
            log.print_log("A config error has occured.", "No 'latitude' or 'longitude' in a 'optional' dict in a 'settings' dict.")
            return
        if automation['data']['startTime'] == 'sunrise':
            startTimeObj = sun.get_sunrise_time()
        else:
            startTimeObj = sun.get_sunset_time()
    startTimeSec = startTimeObj.hour * 3600 + startTimeObj.minute * 60

    stopTimeObj = None
    if automation['data']['stopTime'] not in ['sunrise', 'sunset']:
        stopTimeObj = datetime.strptime(automation['data']['stopTime'], "%H:%M")
    else:
        try:
            sun = Sun(float(settings['optional']['latitude']), float(settings['optional']['longitude']))
        except Exception as e:
            log.print_log("A config error has occured.", "No 'latitude' or 'longitude' in a 'optional' dict in a 'settings' dict.")
            return
        if automation['data']['stopTime'] == 'sunrise':
            stopTimeObj = sun.get_sunrise_time()
        else:
            stopTimeObj = sun.get_sunset_time()
    stopTimeSec = stopTimeObj.hour * 3600 + stopTimeObj.minute * 60
    
    if startTimeSec < stopTimeSec:
        if datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0) + timedelta(seconds = stopTimeSec) < datetime.now():
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 1:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 0)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 1 -> 0")
        elif datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0) + timedelta(seconds = startTimeSec) < datetime.now():
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 0:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 1)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 0 -> 1")
        else:
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 1:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 0)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 1 -> 0")
    else:
        if datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0) + timedelta(seconds = startTimeSec) < datetime.now():
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 0:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 1)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 0 -> 1")
        elif datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0) + timedelta(seconds = stopTimeSec) < datetime.now():
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 1:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 0)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 1 -> 0")
        else:
            if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 0:
                accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 1)
                log.print_log('Scheduler', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "' --- 0 -> 1")