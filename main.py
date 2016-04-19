#!/usr/bin/env python2
import dialogs

def batteryStats(str) :
    getStat = '/sys/class/power_supply/BAT1/' + str
    return open(getStat, 'r').read().strip()

mini = 40
maxi = 80

if (batteryStats('capacity') < str(mini)):
    if (batteryStats('status').lower() == 'discharging'):
        #print "yes"
        dialogs.make('warning', 'Battery level below threshold. Please connect a charger.')

if (int(batteryStats('capacity')) >= maxi):
    if (batteryStats('status').lower() == 'charging'):
        dialogs.make('info', 'Battery levels optimal. Please disconnect the charger.')

if (batteryStats('capacity').lower() == 'full'):
    dialogs.make('info', 'Battery full. Please disconnect the charger.')
