from datetime import time
from random import random, randint

import requests

version = 5.126
token = '4fde78b47f8b09db46a426e36136e6931279c36e2ac5279ab9a01509de5f9a1c113efffbc8ba9b82a5298'
response = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                        params={'access_token': token, 'group_id': 164157228, 'v': version, }).json()['response']
print(response)
data = {'ts': response['ts']}
key = response['key']
server = response['server']


def rep():
    global data, key, server
    response = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                            params={'access_token': token, 'group_id': 164157228, 'v': version, }).json()['response']
    data = {'ts': response['ts']}
    key = response['key']
    server = response['server']


maf = []
a = open('text_mys.txt', 'r')
f = a.read().split('\n')

while True:  # Проверка и обработка запросов
    try:
        data = requests.get(server, params={'act': 'a_check', 'key': key, 'ts': data['ts'], 'wait': 25, }).json()
    except:
        time.sleep(120)
        rep()
        data = requests.get(server, params={'act': 'a_check', 'key': key, 'ts': data['ts'], 'wait': 25, }).json()
    if 'updates' in data:
        for mas in data['updates']:

            if mas['object']['message']['text'].lower() == 'music':


                print(randint(0, len(f) - 1))
                requests.get('https://api.vk.com/method/messages.send', params={'access_token': token, 'v': version,
                                                                                'user_id': mas['object']['message'][
                                                                                    'from_id'], 'random_id': 0,
                                                                                'message': "ог",
                                                                                'attachment': "audio467073495_" + f[
                                                                                    randint(0, len(f) - 1)]})
            else:
                requests.get('https://api.vk.com/method/messages.send', params={'access_token': token, 'v': version,
                                                                                'user_id': mas['object']['message'][
                                                                                    'from_id'], 'random_id': 0,
                                                                                'message': "не напиши слово /music/"})


    else:
        rep()
