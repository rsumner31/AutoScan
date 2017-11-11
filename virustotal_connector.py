import json

from django.utils.datetime_safe import datetime

__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"

import loadstrings
import requests

# Placeholder for you VirusTotal key, look inside Strings.json for an alternative place where you can host the key.
VT_API_KEY = 'Placeholder'

# Load the helper class to print out help text.
_help = loadstrings.loadstrings()


class VirusTotal(object):
    def connect_to_vt(self, ip_address=None):
        _ip_address = ip_address
        url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
        if _ip_address is not None:
            params = {'ip': _ip_address, 'apikey': 'f575ed4296a604aa5ed9fbb52e524744dc160151fcd679799fc57b9cc4f4a775'}
            response = json.loads(json.dumps(requests.get(url, params).json(), ensure_ascii=False))
            # I don't really care for detections that did not happen this year.
            threshold = str(datetime.now().year)
            if response['response_code'] == 1:
                if threshold not in response['resolutions'][0]['last_resolved']:
                    return True
        elif _ip_address is None:
            print(_help.return_help('NoVirusTotal'))
            return False
        else:
            return False


var = VirusTotal()
a = var.connect_to_vt()
print(a)
