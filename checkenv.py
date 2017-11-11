__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"
from importlib import import_module
from sys import version_info

from pip import main

from loadstrings import loadstrings

_help = loadstrings()


class check_env():
    # check_modules checks if the necessary python modules are installed and if not installs them.
    def check_modules(self):
        try:
            import_module('requests')
            import_module('shodan')
        except ImportError as e:
            var = e.__module__
            print(_help.return_help('Module'))
            try:
                main(['install', var])
            except Exception as error:
                print(error)
                return False
        return True

    # Check if we have Python 3.x in order to work
    def check_version(self):
        if version_info >= (3, 0):
            return True
        else:
            print(_help.return_help('Python'))
            return False
