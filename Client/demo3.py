# 向本机运行的服务端发送数据

import paho.mqtt.client as mqtt

# 本机IP地址
HOST = "127.0.0.1"
# 本机服务运行的端口
PORT = 1883

def on_connect(client: mqtt.Client, userdata, flags, rc):
    print("Connect with result code " + str(rc))
    # 注册topic
    client.subscribe("test")

def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    print(msg.topic + " " + msg.payload.decode("utf-8"))

def on_publish(client: mqtt.Client, userdata, result):
    print("data published\n")

def send(topic: str, message: str):
    client = mqtt.Client()
    client.username_pw_set("fjh", "123456")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect(HOST, PORT, 60)
    # qos的等级1,2,3分别对应着3种发送消息方式
    # 0 代表消息只发送一次,可能会丢失
    # 1 代表消息确保送达,但是可能收到多次
    # 2 代表消息确保送到且只收到一次
    client.publish(topic, message, qos=0, retain=False)
    client.loop_forever()

if __name__ == '__main__':
    send("test", "hello i am you")