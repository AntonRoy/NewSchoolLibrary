# -*- coding: utf-8 -*-
import executes_from_bot as ex

class Plugin:
    vk = None

    def __init__(self, vk):
        self.vk = vk
        print('автор')

    def getkeys(self):
        keys = [u'зарезервировать', u'зарезервируй']
        ret = {}
        for key in keys:
            ret[key] = self
        return ret

    def call(self, msg):
       book = msg['text'][1]
       author = msg['text'][2]

       try:
           if ex.reserve(book, author):
               vk.respond(msg, {'message': "Отлично! Книга зарезервирована!"})
           else:
               vk.respond(msg, {'message': "Очень жаль, но книги нет или она была зарезервирована до вас."})
       except:
           vk.respond(msg, {'message': 'Запрос введен неверно.'})