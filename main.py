import threading
from EmulatorGUI import GPIO
import variableAndContrants as env
import led_traffic_controller as traffic
import led_lcd_controller as lcd
import database as api
import time

# Thiết lập mode cho GPIO
GPIO.setmode(GPIO.BCM) 

# Thiết lập các chân GPIO
GPIO.setup(env.RED_1, GPIO.OUT)
GPIO.setup(env.RED_2, GPIO.OUT)
GPIO.setup(env.YELLOW_1, GPIO.OUT)
GPIO.setup(env.YELLOW_2, GPIO.OUT)
GPIO.setup(env.GREEN_1, GPIO.OUT)
GPIO.setup(env.GREEN_2, GPIO.OUT)
GPIO.setup(env.Button, GPIO.IN)

GPIO.setup(env.LED_PIN_A, GPIO.OUT)
GPIO.setup(env.LED_PIN_B, GPIO.OUT)
GPIO.setup(env.LED_PIN_C, GPIO.OUT)
GPIO.setup(env.LED_PIN_D, GPIO.OUT)
GPIO.setup(env.LED_PIN_E, GPIO.OUT)
GPIO.setup(env.LED_PIN_F, GPIO.OUT)
GPIO.setup(env.LED_PIN_G, GPIO.OUT)

GPIO.setup(env.LED_PIN_DP, GPIO.OUT)
GPIO.setup(env.LED_PIN_D1, GPIO.OUT)
GPIO.setup(env.LED_PIN_D2, GPIO.OUT)

# Thiết lập môi trường
api.call()

# Bật chế độ chờ ghi cho LCD
lcd.lcd_init()

# Bật chế độ đèn giao thông
traffic.HandleLED()