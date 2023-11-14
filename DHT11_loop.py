import Adafruit_DHT
import time

# センサーのタイプとピン番号を指定
sensor = Adafruit_DHT.DHT22
pin = 4

try:
    while True:
        # センサーデータを取得
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # データの表示
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
        else:
            print('Failed to retrieve data from the sensor.')

        # 一定の待機時間（ここでは5秒）を挟む
        time.sleep(5)

except KeyboardInterrupt:
    print("Program terminated by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleaning up GPIO")
    # プログラム終了時にGPIOをクリーンアップ
    GPIO.cleanup()
