import json

#min = 40
#max = 80
#config = {'minThreshold': min, 'maxThreshold': max}
#
#with open('config.json', 'w') as f:
#    json.dump(config, f)
#

with open('config.json', 'r') as f:
    config = json.load(f)

    print (config['maxThreshold'])
