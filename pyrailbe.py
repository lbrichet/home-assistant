import urllib.request
import json
import time
from datetime import datetime

ATTR_DEPARTURE_TIME = 'departure time'
ATTR_DEPARTURE_STATION = 'departure station'
ATTR_DEPARTURE_PLATFORM = 'departure platform'
ATTR_DEPARTURE_DELAY = 'departure delay'
ATTR_DEPARTURE_CANCELED = 'departure canceled'
ATTR_ARRIVAL_STATION = 'arrival station'
ATTR_ARRIVAL_PLATFORM = 'arrival platform'
ATTR_ARRIVAL_DELAY = 'arrival delay'
ATTR_ARRIVAL_CANCELED = 'arrival canceled'
ATTR_ARRIVAL_DIRECTION_NAME = 'arrival direction name'
ATTR_DURATION = 'duration'

CONF_URL = 'http://api.irail.be/connections/'
CONF_FROM_STATION = 'namur'
CONF_TO_STATION = 'bruxelles nord'
CONF_DATE = 'today'
CONF_TIME = 'now'
CONF_TIMESEL = 'departure'
CONF_LANG = 'fr'
CONF_FORMAT = 'json'

dt=datetime.now()
if 'today' in CONF_DATE:
    CONF_DATE = dt.strftime('%d')+dt.strftime('%m')+dt.strftime('%y')
if 'now' in CONF_TIME:
    CONF_TIME = dt.strftime("%H%M")

_url=CONF_URL+"?from="+CONF_FROM_STATION+"&to="+CONF_TO_STATION+"&date="+CONF_DATE+"&time="+CONF_TIME+"&timesel="+CONF_TIMESEL+"&format="+CONF_FORMAT+"&lang="+CONF_LANG

# print(_url)

_query=urllib.request.urlopen(_url)
mydict = json.loads(_query.read().decode())

for id in mydict['connection']:
    ATTR_DEPARTURE_TIME = str(datetime.fromtimestamp(int(id['departure']['time'])).time())
    ATTR_DEPARTURE_STATION = id['departure']['station']
    ATTR_DEPARTURE_PLATFORM = id['departure']['platform']
    ATTR_DEPARTURE_DELAY = float(id['departure']['delay'])/60
    ATTR_DEPARTURE_CANCELED = id['departure']['canceled']
    ATTR_ARRIVAL_STATION = id['arrival']['station']
    ATTR_ARRIVAL_PLATFORM = id['arrival']['platform']
    ATTR_ARRIVAL_DELAY = float(id['arrival']['delay'])/60
    ATTR_ARRIVAL_CANCELED = id['arrival']['canceled']
    ATTR_ARRIVAL_DIRECTION_NAME = id['arrival']['direction']['name']
    ATTR_DURATION = float(id['duration'])/60
    print(ATTR_DEPARTURE_TIME+" - "+ATTR_DEPARTURE_STATION+" - "+ATTR_DEPARTURE_PLATFORM+" - "+str(ATTR_DEPARTURE_DELAY)+" - "+ATTR_DEPARTURE_CANCELED+" - "+ATTR_ARRIVAL_STATION+" - "+ATTR_DEPARTURE_PLATFORM+" - "+str(ATTR_ARRIVAL_DELAY)+" - "+ATTR_ARRIVAL_CANCELED+" - "+ATTR_ARRIVAL_DIRECTION_NAME+" - "+str(ATTR_DURATION))
