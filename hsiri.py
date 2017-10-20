#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, Job
from datetime import datetime
import re

def timeStringToSec(s):
    p = re.compile('((\d*)h)?((\d*)m)?(\d*)s?')
    m = p.match(s)
    hours = 0 if not m.group(2) else int(m.group(2))
    minutes = 0 if not m.group(4) else int(m.group(4))
    seconds = 0 if not m.group(5) else int(m.group(5))
    return 3600 * hours + 60 * minutes + seconds
    

def timerHandler(bot, update, args, job_queue):

    def callback_alarm(bot, job):
        bot.send_message(chat_id=job.context[0], text=job.context[1])

    chat_id = update.message.chat_id
    timerSec = timeStringToSec(args[0])
    print("{} set a timer for {} secs".format(chat_id, timerSec))
    message = "[Timer Alarm]"
    if len(args) > 1:
        for m in args[1:]:
            message = message + " " + m
    job = Job(callback_alarm, timerSec, repeat=False, context=(chat_id, message))
    job_queue.put(job)

def logHandler(bot, update):
    msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + update.message.text.split(' ', 1)[1]
    filename = update.message.from_user['username'] + '_log.txt'
    with open(filename, 'a') as f:
        f.write(msg)


def loadToken(filename='TOKEN'):
    with open(filename) as f:
        return (f.read().splitlines())[0]


if __name__ == '__main__':
    token = loadToken('TOKEN')
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('timer',
                                          timerHandler,
                                          pass_args=True,
                                          pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('log', logHandler))
        
    updater.start_polling()
    updater.idle()

