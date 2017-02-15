# -*- coding: utf-8 -*-
import executes_from_bot

class Plugin:
    vk = None

    def __init__(self, vk):
        self.vk = vk
        print('Наличие книги')

    def getkeys(self):
        keys = [u'наличие', 'книга']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg):
        request = msg['body'].split()
        try:
            bl = executes_from_bot.Book_In_Library(request[1], request[2])
            self.vk.respond(msg, {'message': 'Книга в библиотеке'})
        except:
            self.vk.respond(msg, {'message': "Извините, но данной книги нет в библиотеке"})