import locale
import json
import os
from pathlib import Path


class Lang:
    def __init__(self):
        l,_ = locale.getdefaultlocale()
        l = l.lower()[0:2]
        self.lang = 'default'
        fn = Path(os.path.dirname(os.path.realpath(__file__)))
        fn = fn / 'lang.json'
        if os.path.isfile(fn):
            with open(fn, encoding='utf-8') as f:
                self.dic = json.load(f)
            values = list(self.dic.values())
            if l in values[0]:
                self.lang = l
        else:
            self.dic = {}

    def tr(self,s):
        if s in self.dic:
            return self.dic[s][self.lang]
        else:
            return s



