import paho.mqtt.client as mqttclient
import time

connected=False
Messagerecieved=False

broker_address="lambda.dgreat.cc"
broker_port=1880
user="user"
password="1234"
topic="test"

def on_connect(client, userdata, flags, rc):
    if rc==0
        print("Client is connected")
        global connected
        connected=True
    else:
        print("Client is NOT connected")

def on_message(client, userdata, message):
    print("Message recieved ", str(message.payload.decode("utf-8")))
    print("Message topic = ", message.topic)

client = mqttclient.Client("MQTT")
client.username_pw_set(user, password=password)
client.on_connect=on_connect
client.connect(broker_address, port=broker_port)
client.loop_start()
client.subscribe(topic)
while connected!=True:
    time.sleep(0.5)
while Messagerecieved!=True:
    time.sleep(0.2)

client.loop_stop()