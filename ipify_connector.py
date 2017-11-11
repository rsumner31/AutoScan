__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"

from requests import get


class ipify(object):
    def ipify_resolver(self, ip=None):
        conn = get('https://api.ipify.org')
        if conn.status_code == 200:
            _ip = conn.text
            if ip is None:
                return _ip
            elif ip is not None:
                _ip = ip
                return _ip
        else:
            return False
