

import requests


url = 'https://www.toutiao.com/api/pc/list/feed'

params = {
    'channel_id': '0',
    'max_behot_time': '1734070705',
    'offset': '0',
    'category': 'pc_profile_recommend',
    'aid': '24',
    'app_name': 'toutiao_web',
    'msToken': 'w4YWPfFN0vbwzDLT6IF-s_Z0jB2l74amgze2ae2VoAk6Q1U3JNfOskDT6AFZRLXPByeCxEZBzxkDyl0Ee3ta4TZPAbFSEfmUxX5Gji2-j08KSNzTGm8C6A==',
    'a_bogus': 'dy8MQDwhmEDpfd6d53KLfY3qV5F3Y0wl0t9bMDhq5dvJYg39HMOv9exYQZUv5DjjNG/pIemjy4haT3CkrQAnM36UHuXLUdQ2myYpKl5Q5xS7516etLWsE0so5ib3SFHp57NUics0y75eKYT0AIcj5JIlODaSYrtswyG7GflNv9smMf=='
}

headers = {
    'cookie': '__ac_nonce=0675bf2800066fa945708; __ac_signature=_02B4Z6wo00f01LN9geAAAIDAhFlFv1szSdizXYVAAEuJdb; tt_webid=7447812951829120548; gfkadpd=24,6457; ttcid=141b1d752bb64f86a51d37be5d2636ea36; x-web-secsdk-uid=ac451518-9001-4f46-b9b7-31a2b1934d3c; local_city_cache=%E6%88%90%E9%83%BD; csrftoken=208972af9d1f5d31a204cb2ba5eac33a; _ga_QEHZPBE5HH=GS1.1.1734079107.1.0.1734079107.0.0.0; _ga=GA1.1.870145932.1734079108; tt_scid=omd-LLTlEFvHFxRJapdyt9lbWEyqkFB0uSS8hgIfk48zmWQlvMzEXL.Rkb5dtl0o8c55; ttwid=1%7CLDbfW13uOdPvNhdHk-99QJINNIGF1uhAtXfN8wl02JY%7C1734079107%7C2a593da1a2461709a73c57dfc9e096f73aa10efb50db5c0781fe28c1c7e3e746; s_v_web_id=verify_m4mhxf36_YdkUd0K2_FPf9_4sGA_BcMK_ANurLfwHYQn0',
    'referer': 'https://www.toutiao.com/?wid=1734079106061',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

html = requests.get(url, params=params, headers=headers)

for i in html.json()['data']:
    print('/n',i)