import os
import os.path
import sys
import time
import urllib.parse as up
from shutil import which

import requests
from tdameritrade import TDClient
from tdameritrade import auth
#auth.authentication(os.environ["TDAMERITRADE_CLIENT_ID"], os.environ["TDAMERITRADE_CALLBACK_URL"])

tdc = TDClient()
# tdc.hours()
print(tdc.options('SPX'))
