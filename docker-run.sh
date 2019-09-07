# subindo o mosquitto

docker run -it -p 1883:1883 -p 9001:9001 -v /mosquitto/data --name mosquitto --restart always -d eclipse-mosquitto
echo "broker mosquito iniciado na rede  wifi local no ip " $(ifconfig wlan0 | grep 'inet ' | cut -d: -f2 | awk '{print $2}')
echo "broker mosquito iniciado na rede  cabeada local no ip " $(ifconfig eth0 | grep 'inet ' | cut -d: -f2 | awk '{print $2}')

# docker run application
docker run -p 8000:80 -v /app --name app -d mqtt-flask-hello-world:0.8