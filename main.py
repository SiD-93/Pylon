#!/usr/bin/env python2
import dialogs

def batteryStats(str) :
    getStat = '/sys/class/power_supply/BAT1/' + str
    return open(getStat, 'r').read().strip()

#batteryStats('capacity')

mini = 40
maxi = 80

if (batteryStats('capacity') < str(mini)):
    if (batteryStats('status').lower() == 'discharging'):
        #print "yes"
        dialogs.make('warning', 'Battery level below threshold. Please connect a charger.')
#dialogs.make('error', 'Hello, world!')

if (batteryStats('capacity') >= str(maxi)):
    if (batteryStats('status').lower() == 'charging'):
        dialogs.make('info', 'Battery level at optimum. Please disconnect the charger.')
