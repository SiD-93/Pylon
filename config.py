import json, os.path

config = { }

def confWrite():
    minimum = raw_input('Enter the minimum threshold: ')
    maximum = raw_input('Enter the maximum threshold: ')
    config = {'minThreshold': minimum, 'maxThreshold': maximum}
    with open('config.json', 'w') as f:
        json.dump(config, f)
        f.close()

def confRead(confValue):
    with open('config.json', 'r') as f:
        config = json.load(f)
        print config[confValue]
        f.close()

if (os.path.exists('./config.json')) == False:
    confWrite()

confRead('minThreshold')
