import Adafruit_DHT

# センサーのタイプとピン番号を指定
sensor = Adafruit_DHT.DHT22
pin = 14

# センサーデータを取得
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
else:
    print('Failed to retrieve data from the sensor.')
