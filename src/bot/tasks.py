import slacky
from celery import shared_task

from . import ai, utils


@shared_task
def slack_message_task(message, channel_id=None, user_id=None, thread_ts=None):
    # openai_msg = utils.chat_with_openai(message, raw=False)
    # print(message, openai_msg)
    pdf_ai_msg = ai.query(message, raw=False)
    r = slacky.send_message(pdf_ai_msg, channel_id=channel_id, user_id=user_id, thread_ts=thread_ts)
    return r.status_code