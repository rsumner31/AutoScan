__author__ = "Fausto Oliveira"
__copyright__ = "Copyright 2017, Fausto Oliveira"
__credits__ = ["Shodan, ipify"]
__license__ = "MIT"
__version__ = "0.99"
__maintainer__ = "Fausto Oliveira"
__status__ = "Production"

import shodan

import ipify_connector
import loadstrings

# Placeholder for you Shodan key, look inside Strings.json for an alternative place where you can host the key.
SHODAN_API_KEY = 'Placeholder'
# Load the helper class to print out help text.
_help = loadstrings.loadstrings()

class Shodan(object):
    def shodan_start(self):
        if SHODAN_API_KEY is not None and 'Placeholder' not in SHODAN_API_KEY:
            _api = shodan.Shodan(SHODAN_API_KEY)
            return _api
        else:
            print(_help.return_help('Shodan'))
            return None

    def shodan_verify(self):
        _api = self.shodan_start()
        _ipify = ipify_connector.ipify()
        _ip = _ipify.ipify_resolver()
        if _api is not None and _ip is not None:
            try:
                _host = _api.host(_ip)
                print(
                    """
                            IP: %s
                            Organization: %s
                            Operating System: %s
                    """ % (_host['ip_str'], _host.get('org', 'n/a'), _host.get('os', 'n/a')))

            except shodan.APIError as e:
                # I want to convert the exception into a string to make it more user friendly
                exception = str(e)
                if 'No information' in exception:
                    print(_help.return_help('NoDetection'))
                else:
                    print('Error: %s' % exception)
            else:
                print(_help.return_help('NoShodan'))
