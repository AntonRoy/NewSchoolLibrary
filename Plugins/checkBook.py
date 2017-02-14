# -*- coding: utf-8 -*-
import executes_from_bot

class Plugin:
    vk = None

    def __init__(self, vk):
        self.vk = vk
        print('Долги')

    def getkeys(self):
        keys = [u'наличие']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg):
        request = msg['body'].replace(u'наличие').replace(u'чб').split(" ")
        try:
            bl = executes_from_bot.Book_In_Library(request[0]. request(1))
            self.vk.respond(msg, {'message': str(bl)})
        except:
            self.vk.respond(msg, {'message': "Точно то написал"})