from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from pathlib import Path
import datetime
import logging
from dotenv import load_dotenv


logger = logging.getLogger(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ['SLACK_TOKEN'])

channel_id="ord-med-kompisar"
spel_lista= ["Wordle","Worldle","Globle","Heardle","Dordle","Waffle","Factle"]
for i in range(1,158):
    today = datetime.datetime.now() + datetime.timedelta(days=i)
    scheduled_time = datetime.time(hour=7,minute=0)
    schedule_timestamp = datetime.datetime.combine(today, scheduled_time).strftime('%s')
    for m in spel_lista:
        try:
            result = client.chat_scheduleMessage(
                channel=channel_id,
                text = f"{m}, {today}",
                post_at=schedule_timestamp
            )
            logger.info(result)
        except SlackAPIError as e:
            logger.error(e)