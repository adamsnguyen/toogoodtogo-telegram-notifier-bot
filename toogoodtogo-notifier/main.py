from telethon.tl.types import Channel
from tgtg import TgtgClient
from telethon import TelegramClient, events, sync, functions, types
from datetime import datetime
import config
import time as tm

# setup

tgtg_client = TgtgClient(email=config.tgtg['email'], access_token=config.tgtg['access_token'],
                    refresh_token=config.tgtg['refresh_token'],
                    user_id=config.tgtg['user_id'])

telegram_client = TelegramClient('TooGoodToGO Notifier', config.telegram['api_id'], config.telegram['api_hash'])
telegram_client.start(bot_token=config.telegram["bot_token"])
# telegram_client(functions.account.ResetAuthorizationRequest(hash=-12398745604826))
# telegram_client.log_out()

print(telegram_client.session.list_sessions())

already_notified = {}

while True:

    try:

        update = tgtg_client.get_items()

        for i in update:
            if int(i['items_available']) == 0 and i['display_name'] in already_notified:
                del already_notified[i['display_name']]

            if (i['items_available'] > 0 and i['display_name'] not in already_notified) or (
                    i['display_name'] in already_notified and int(already_notified[i['display_name']]) != int(i['items_available'])
                    and int(i['items_available'] > 0)):
                already_notified[i['display_name']] = i['items_available']
                now = str(datetime.today().strftime("%I:%M %p"))
                message = f"**{i['display_name']}** is available! (Items available:**{i['items_available']}**, Time:{now})"
                result = telegram_client.send_message(entity=config.telegram['channel_id'], message = message, silent=False)
                print(message)

    except Exception as e:
        print("Issues with Internet Connection...")
        print(e)
        tgtg_client = TgtgClient(email=config.tgtg['email'], access_token=config.tgtg['access_token'],
                    refresh_token=config.tgtg['refresh_token'],
                    user_id=config.tgtg['user_id'])
        telegram_client.start(bot_token=config.telegram["bot_token"])


    tm.sleep(5)


    

