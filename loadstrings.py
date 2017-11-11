__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"
import json
from locale import getdefaultlocale

''' 
    This class is currently only used as a L10N component but look inside the Strings.json
    and you can see that I have other uses for this such as returning API keys.
'''


class loadstrings(object):
    def get_locale(self):
        # An hacky way of getting just the language without the culture
        return getdefaultlocale()[0][0:2]

    def load_json(self):
        # We want to provide various strings from the JSON file so this will load it.
        try:
            _file = open('Strings.json', 'r')
            _json = json.loads(_file.read())
            return _json
        except FileNotFoundError as e:
            print('Cannot open Strings.json due to {}'.format(e))
            return None

    def return_help(self, section):
        _language = self.get_locale()
        _help = self.load_json()

        if _help is not None and section is not None and _language in _help:
            print(str(_help[_language][section]).strip('[]'))
        else:
            print("Cannot find this text")
