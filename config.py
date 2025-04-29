import configparser
from collections import defaultdict
import re
import random

EMAIL = "email"
PASSWORD = "password"

def read_config():
    config = configparser.ConfigParser(strict=False)
    config.read('config.ini')

    email = config.get('user_info', 'email')
    password = config.get('user_info', 'password')

    oasis = [value
             for key, value in config.items('user_info')
             if key == 'oasis']
    
    natares = [value
             for key, value in config.items('user_info')
             if key == 'natares']
    
    towns = [value
             for key, value in config.items('user_info')
             if key == 'towns']
    
    min_troops_a = config.get('user_info', 'min_troops_a')

    min_troops_b = config.get('user_info', 'min_troops_b')
    
    windowless = config.getboolean('user_info', 'windowless')


    config_values = {
        'email': email,
        'password': password,
        'oasis': oasis,
        'natares': natares,
        'towns': towns,
        'min_troops_a': min_troops_a,
        'min_troops_b': min_troops_b, 
        'windowless': windowless
    }
    return extract_farm_pairs(config_values)

def extract_farm_pairs(user_info):
    oasis_list = user_info.get('oasis', [])
    combined = ','.join(oasis_list)
    oasis_matches = re.findall(r'\(\s*(-?\d+)\s*\|\s*(-?\d+)\s*\)', combined)

    natare_list = user_info.get('natares', [])
    combined = ','.join(natare_list)
    natare_matches = re.findall(r'\(\s*(-?\d+)\s*\|\s*(-?\d+)\s*\)', combined)

    towns_list = user_info.get('towns', [])
    combined = ','.join(towns_list)
    towns_list = re.findall(r'\(\s*(-?\d+)\s*\|\s*(-?\d+)\s*\)', combined)

    user_info['oasis'] = [(int(x), int(y)) for x, y in oasis_matches]
    user_info['natares'] = [(int(x), int(y)) for x, y in natare_matches]
    user_info['towns'] = [(int(x), int(y)) for x, y in towns_list]
    random.shuffle(user_info['oasis'])
    random.shuffle(user_info['natares'])
    random.shuffle(user_info['towns'])

    return user_info