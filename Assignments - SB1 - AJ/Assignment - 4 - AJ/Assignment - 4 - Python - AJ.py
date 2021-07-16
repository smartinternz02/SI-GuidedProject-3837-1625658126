import wiotp.sdk.device
import time
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
    print("Username Recieved from the APP: ",cmd.data['Username'])
    print("Password Recieved from the APP: " ,cmd.data['Password'])
    
    
try:
    client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
    client.connect()
    while True:
        client.commandCallback = myCommandCallback
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()