# 接受在本机运行的服务端的消息
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

def client_loop():
    # id注意要保持唯一
    client_id = "1"
    client = mqtt.Client(client_id)
    client.username_pw_set("admin", "123456")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    client_loop()