#!/usr/bin/env python2
import config, os.path
from pythonzenity import *
def batteryStats(str) :
    getStat = '/sys/class/power_supply/BAT1/' + str
    return open(getStat, 'r').read().strip()

if (os.path.exists('./conf.json')) == False:
    setConf = Question(title='Ampyre', text='No defaults set. Set now?')
    if setConf == -8:
        config.confWrite()
    else:
        Error(title='Ampyre', text='No defaults set.')

if (batteryStats('capacity') < str(config.confRead('minThreshold'))):
    if (batteryStats('status').lower() == 'discharging'):
        Error(title='Ampyre', text='Battery level below threshold. Please connect a charger.')

if (int(batteryStats('capacity')) > int(config.confRead('maxThreshold'))):
    if (batteryStats('status').lower() == 'charging'):
        Message(title='Ampyre', text='Battery levels optimal. Please disconnect the charger.')

if (int(batteryStats('capacity')) == 100):
    if (batteryStats('status').lower() == 'full'):
        Message(title='Ampyre', text='Battery full. Please disconnect the charger.')
