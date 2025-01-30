# Raspberry-Plant-Watering
*a HTL Rankweil project*

This project allows you to water your favorite plants automatically when they are thirsty. The heart of the project is a Raspberry Pi 4B, which functions as a web server, controls the pump, and reads the sensor values. And there is also a web interface, which provides you with a good overview of your plants' conditions.

## Wiring for the modules:

![Wiring picture]({9465958C-4048-4FA6-8F26-22932DBCA2F0}.png)

## Used products:
* Raspberry Pi 4B: [2GB RAM](https://www.berrybase.at/raspberry-pi-4-computer-modell-b-2gb-ram)
* Moisture sensor: [Adafruit STEMMA Soil Sensor](https://www.adafruit.com/product/4026)
* DC-Motor driver: [MX1508](https://de.aliexpress.com/item/1005002431361324.html?gatewayAdapt=glo2deu)
* Pump: [Diaphragm pump 6V](https://de.aliexpress.com/item/1005004761121166.html?spm=a2g0o.order_list.order_list_main.5.27f25c5fnGL01o&gatewayAdapt=glo2deu)
* Ultrasonic distance sensor: [HC-SR04](https://www.sparkfun.com/ultrasonic-distance-sensor-3-3v-hc-sr04.html)


## Installation Steps:

**1. Update and Setup your Raspberry Pi**
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip git
```
**2. Clone the project repository**
```
git clone https://github.com/your-repo/raspberry-plant-watering.git
cd raspberry-plant-watering
```
**3. Install required Python libraries**
```
pip install -r requirements.txt
```

## Connecting to the Web Server

**Starting the Flask Server**\
To start the Flask web server, use the following command:
```bash
flask --app server.py run --host=0.0.0.0
```
\
**Running on a Different Port (Optional)**\
By default, Flask runs on port 5000. To use a different port (e.g., 8080), run:
```bash
flask --app server.py run --host=0.0.0.0 --port=8080
```
\
**Accessing the Web Server**

**From the Raspberry Pi itself**\
Open a browser and go to:
```
http://127.0.0.1:5000
```
\
**From Another Device on the Same Network**\
Use the Raspberry Pi's local IP:
```
http://<raspberry_pi_ip>:5000
```