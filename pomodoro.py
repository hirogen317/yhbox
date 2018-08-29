import os
from datetime import datetime, timedelta, date
import time
import logging

"""
Start / Stop in fixed time, no setting allowed.

xx:50 -> Pomodoro stop, record.
xx:00 -> New Pomodoro start.
"""

FROG_SOUND = "/System/Library/Sounds/Frog.aiff"
LOG_BASE = "~/Documents/documents/work/dailylogs"

log_path = '{}/{}'.format(LOG_BASE , date.today().strftime('%m'))


if not os.path.exists(log_path):
    os.makedirs(log_path)

log_file = os.path.join(log_path, "worklog_{}.log".format( date.today().strftime('%Y%m%d')))

logging.basicConfig(level = logging.INFO, log_file = filename, format="%(asctime)s %(message)s")


def frog():
    os.system("afplay -t 1 {}".format(FROG_SOUND))


def log():
    msg = input("Record your action last hour:")
    logging.info('[LAST] ' + msg)
    msg = input("Estimate your action next hour:")
    logging.info('[NEXT] ' + msg)

nowtime = datetime.now()
original_hour = nowtime.replace(microsecond=0, second=0, minute=0)
#nexthour = nowhour + timedelta(hours=1)

not_sounded = True

while True:
    time.sleep(1)
    if datetime.now().hour != original_hour:
        frog()
        original_hour = datetime.now().hour
        not_sounded = True
        print('新しいpomodoro始まりますよ:{hour}. 頑張れ！'.format(hour= original_hour))
    if datetime.now().minute == 50 and datetime.now().second <= 1 and not_sounded:
        frog()
        print('お疲れ様でした！Pomodoro {hour} 終わりました。記録しましょう。'.format(hour = original_hour))
        not_sounded = False
        log()
