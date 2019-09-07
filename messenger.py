import paho.mqtt.client as mqtt #import the client1
import datetime
default_port=1883
#
# def my_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         # doesn't even have to be reachable
#         s.connect(('10.255.255.255', 1))
#         IP = s.getsockname()[0]
#     except Exception as e:
#         print("Impossível encontrar IP, há conexão com a rede?")
#         print(e)
#         # print("Impossível encontrar IP, há conexão com a rede?")
#         IP = '127.0.0.1'
#     finally:
#         s.close()
#     print('IP='+ IP)
#     return IP

broker_address = "192.168.15.12"

def on_message(client, userdata, message):
    print("time ", datetime.datetime.now())
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    formated_message = str(datetime.datetime.now()) + "- Received message: "+ str(message.payload.decode("utf-8")) + ", on topic: " + str(message.topic) + "\n"
    print(formated_message)
    f = open("messages.log", "a+")
    f.write(formated_message)
    f.close()
    print("escreveu")

def read_message():
    try:
        f = open("/app/messages.log", "r+")
        message = f.read()
        f.close()
    except Exception as e:
        message = "No messages found"
    return message

def on_connect():
    print("Conectado")


def subscribe_on_topic(topic = "/topic/teste"):

    #broker_address="iot.eclipse.org"
    # client = connect_to_broker(mc.ip(), mc.name(), mc.cert_name())
    client = mqtt.Client("subscriber7")
    client.on_message = on_message  # attach function to callback
    client.on_connect = on_connect  # attach function to callback
    print("connecting to broker: " + broker_address)
    client.connect(broker_address, port=default_port) #connect to broker
    client.loop_start()  # start the loop
    print("Subscribing to topic: " + topic)
    client.subscribe(topic)

def publish_on_topic(topic = "/topic/teste", message = '"hello":"world"'):

    #broker_address="iot.eclipse.org"
    client = mqtt.Client("publisher")
    client.on_message = on_message  # attach function to callback
    client.on_connect = on_connect  # attach function to callback
    print("connecting to broker: " + broker_address)
    client.connect(broker_address, port=default_port) #connect to broker
    client.loop_start()  # start the loop
    print("Publishing message: "+message+"\nto topic: " + topic)
    client.publish(topic,message)
    client.loop_stop()  # start the loop
    client.disconnect()
