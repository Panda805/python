import configparser
config = configparser.ConfigParser()
config.read('setting.ini')
ipArray=config.items('CAM')
if not ipArray:
    exit(-1)
for i in range(len(ipArray)):
    if not ipArray[i][1]:
        continue
    print(ipArray[i])
    
y=(())
for i in range(len(ipArray)):
    x=((ipArray[i][1],config),)
    y += x
print(y)