import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "0gzb6e",
        "typeId": "18BEC1278_1A_SB1",
        "deviceId":"15201"
    },
    "auth": {
        "token": "1520ANDREW1"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    

try:
    client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
    client.connect()

    while True:
        inten=random.randint(0,100)
        water=random.randint(0,100)
        myData={'wl':water, 'li':inten}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()