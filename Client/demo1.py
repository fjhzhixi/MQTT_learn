import paho.mqtt.client as mqtt
# 官网的demo
def on_connect(client: mqtt.Client, userdata, flags, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("$SYS/#")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    # 打印从Broker获得的message
    print(msg.topic + " " + str(msg.payload))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_forever()



