#!/usr/bin/env python2

# To check for config file and to read/write to it.
import os, json
# To generate PyGTK dialogs.
from pythonzenity import *

# Begin global value definitions.

# Current user's home directory.
home = os.environ['HOME']
# Default configuration directory.
confDir = home + '/.config/ampyre'

####################################
# Begin Configuration file handling.
####################################

def confWrite():

    #Check if directory exists; if not, make it.
    if not os.path.exists(confDir):
        os.makedirs(confDir)

    # Accept lower threshold from user.
    lower = Entry(title='Ampyre Config', text='Enter the lower threshold: ')
    # Accept upper threshold from user.
    upper = Entry(title='Ampyre Config', text='Enter the upper threshold: ')

    # Check if either value hasn't been entered.
    if (lower == '' or upper == ''):
        Warning(title='Ampyre Config', text='Threshold(s) not set. Please set to continue.')
        # Try to get values again.
        confWrite()
    else:

        # Write values to the configuration dictionary.
        config = {
        'lowThreshold': lower,
        'upThreshold': upper
        }

        # Open configuration file for writing.
        with open(confDir+'/config.json', 'w') as f:
            json.dump(config, f)
            # Close file after writing.
            f.close()
        # Let user know config has been written.
        Message(title='Ampyre Config', text='Thresholds set.')

def confRead(attrib):

    # Open configuration file for reading.
    with open(confDir+'/config.json', 'r') as f:
        config = json.load(f)
        # Return required configuration attribute.
        return config[attrib]
        # Close file after reading.
        f.close()

####################################
# Begin obtaining battery attributes.
####################################

def batteryStats(str) :
    # Obtain attribute from user.
    getStat = '/sys/class/power_supply/BAT1/' + str
    # Return battery attribute.
    return open(getStat, 'r').read().strip()

####################################
# Begin checking battery attributes.
####################################

def main():

    # If configuration file is not present or is not readable.
    if (os.path.exists(confDir+'/config.json')) == False:
        # Ask user to create one.
        setConf = Question(title='Ampyre', text='No thresholds set. Set now?')
        # -8 is the return value of the 'Yes' dialog button.
        if setConf == -8:
            # Call confWrite() directly to create a new configuration file.
            confWrite()
        else:
            # Warn user and quit.
            Error(title='Ampyre', text='No defaults set.')

    if (batteryStats('capacity') < str(confRead('lowThreshold'))):
        if (batteryStats('status').lower() == 'discharging'):
            Error(title='Ampyre', text='Battery level below threshold. Please connect a charger.')

    if (int(batteryStats('capacity')) > int(confRead('upThreshold'))):
        if (batteryStats('status').lower() == 'charging'):
            Message(title='Ampyre', text='Battery levels optimal. Please disconnect the charger.')

    if (int(batteryStats('capacity')) == 100):
        Message(title='Ampyre', text='Battery full. Please disconnect the charger.')
main()
