__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"

from requests import get


class ipify(object):
    def ipify_resolver(self):
        ip = get('https://api.ipify.org').text
        if ip is not None:
            return ip
