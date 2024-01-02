from datetime import datetime, timedelta

import database, log

# check if device should be turned off
def timer(automation: dict, accessories_database: database.Database) -> None:
    if accessories_database.get_accessory_value(automation['uniqueId'], automation['characteristic']) == 1:
        if accessories_database.get_accessory_date(automation['uniqueId']) + timedelta(seconds = int(automation['data']['period'])) < datetime.now():
            accessories_database.set_accessory_value(automation['uniqueId'], automation['characteristic'], 0)
            log.print_log('Timer', "'" + accessories_database.get_accessory_serviceName(automation['uniqueId']) + "' --- '" + automation['characteristic'] + "'")

