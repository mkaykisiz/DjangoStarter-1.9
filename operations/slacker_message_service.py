# coding=utf-8

from slacker import Slacker


def slacker_send_error(errorline, e):
    slack = Slacker('api_key')
    message = 'Error on line' + str(errorline) + ' HATA : ' + '%s (%s)' % (e, type(e))
    slack.chat.post_message('#channel', message)


def slack_payment_message(message):
    slack = Slacker('api_key')
    slack.chat.post_message('#channel', message)