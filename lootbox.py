token = input("Copy and paste user token: ")

import requests, json, base64, time

X_Super = {"client_build_number":280346}

headers = {
    'authorization': token,
    'x-super-properties': base64.b64encode(json.dumps(X_Super).encode('utf-8')).decode('utf-8'),
}

o=0
ui = 0
while True:
    response = requests.post('https://discord.com/api/v9/users/@me/lootboxes/open', headers=headers)
    if 'user_lootbox_data' in response.json():
        if 'opened_items' in response.json()['user_lootbox_data']:
            ui = sum(response.json()['user_lootbox_data']['opened_items'].values())+70
    if 'opened_item' in response.json():
        o += 1
        print("[AutoLootbox] >> Item Opened!", response.json()['opened_item'], "Total Opened:",o, "Inventory Items:", ui)
    if "retry_after" in response.json():
        time.sleep(response.json()["retry_after"])