__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"

import checkenv
import shodan_connector

_checkenv = checkenv.check_env()
_shodan_connector = shodan_connector.Shodan()

if __name__ == '__main__':
    if _checkenv.check_version() and _checkenv.check_modules():
        _shodan_connector.shodan_verify()
