import requests
from datetime import datetime, timedelta

import log

hb_url = None

access_token = None
expiration_date = None

headers = None

# get access token & its expiration time
def get_access_token(config: dict) -> None:
    global hb_url, access_token, expiration_date, headers

    if hb_url == None:
        hb_url = "http://" + config['settings']['ip'] + ":" + config['settings']['port']

    if expiration_date != None and access_token != None and headers != None:
        if datetime.now() + timedelta(seconds = 100) < expiration_date:
            response = requests.get(hb_url + "/api/auth/check", headers = headers)
            if response.json().get('status') == 'OK':
                return

    data = {
        'username': config['settings']['username'],
        'password': config['settings']['password']
    }

    response = requests.post(hb_url + "/api/auth/login", json = data)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception('Could not authorize using the username/password provided.')
    
    if access_token == None:
        log.print_log('An authentication token has been received.')
    else:
        log.print_log('An authentication token has been refreshed.')

    response = response.json()
    access_token = response.get('access_token')
    expiration_date = datetime.now() + timedelta(seconds = response.get('expires_in'))
    headers = {'Authorization': f'Bearer {access_token}'}

    return

# get list of accessories
def get_accessories() -> list:
    global hb_url, headers

    response = requests.get(hb_url + "/api/accessories", headers = headers)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception('Could not authorize using the username/password provided.')

    return response.json()

# get list of accessories layout
def get_accessories_layout() -> list:
    global hb_url, headers

    response = requests.get(hb_url + "/api/accessories/layout", headers = headers)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception('Could not authorize using the username/password provided.')

    return response.json()

# print info about error during requesting to Homebridge API
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while requesting the Homebridge API.", str(e))