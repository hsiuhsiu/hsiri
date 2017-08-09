#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, Job


def timerHandler(bot, update, args, job_queue):

    def callback_alarm(bot, job):
        bot.send_message(chat_id=job.context[0], text=job.context[1])

    chat_id = update.message.chat_id
    timerSec = int(args[0])
    print("{} set a timer for {} secs".format(chat_id, timerSec))
    message = "[Timer Alarm]"
    if len(args) > 1:
        for m in args[1:]:
            message = message + " " + m
    job = Job(callback_alarm, timerSec, repeat=False, context=(chat_id, message))
    job_queue.put(job)


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
        
    updater.start_polling()
    updater.idle()

