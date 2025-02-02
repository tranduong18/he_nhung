import variableAndContrants as env
import led_7seg_controller as seg
import led_lcd_controller as lcd
import threading as cpu
from EmulatorGUI import GPIO
import time
import database as api

def HandleLED():
    theard_read_button = cpu.Thread(target=readButton, args=(env.IS_Emer,))
    theard_read_button.start()
    while True:
        if env.IS_Night[0]:  # Bật chế độ ban đêm
            lcd.lcd_night_mod()
            seg.off_led()
            while env.IS_Night[0]:
                # print(env.IS_Night[0])
                print("Đèn vàng ban đêm")
                onEmer(env.TIME_EMER[0])
        else:   # Bật chế độ giao thông bình thường
            handelEmer(env.IS_Emer[0])
            lcd.lcd_string(env.INFO_SHOW[0], 2)
            onGreen(1)
            onRed(2)
            seg.count_down(env.GREEN_1)
            if env.IS_Night[0]:
                continue
            
            handelEmer(env.IS_Emer[0])
            lcd.lcd_string(env.INFO_SHOW[0], 2)
            onYellow(1)
            seg.count_down(env.YELLOW_1)
            if env.IS_Night[0]:
                continue
            
            handelEmer(env.IS_Emer[0])
            lcd.lcd_string(env.INFO_SHOW[0], 2)
            onRed(1)
            onGreen(2)
            seg.count_down(env.GREEN_2)
            if env.IS_Night[0]:
                continue

            handelEmer(env.IS_Emer[0])
            lcd.lcd_string(env.INFO_SHOW[0], 2)
            onYellow(2)
            seg.count_down(env.YELLOW_2)
            if env.IS_Night[0]:
                continue

def onRed(index):
    if index == 1:
        GPIO.output(env.YELLOW_1, 0)  
        GPIO.output(env.GREEN_2, 0)
        GPIO.output(env.RED_1, 1)
    if index == 2:
        GPIO.output(env.YELLOW_2, 0)
        GPIO.output(env.GREEN_2, 0)
        GPIO.output(env.RED_2, 1)

def onYellow(index):
    if index == 1:
        GPIO.output(env.YELLOW_1, 1)
        GPIO.output(env.GREEN_1, 0)
        GPIO.output(env.RED_1, 0)
    if index == 2:
        GPIO.output(env.YELLOW_2, 1)
        GPIO.output(env.GREEN_2, 0)
        GPIO.output(env.RED_2, 0)

def onGreen(index):
    if index == 1:
        GPIO.output(env.YELLOW_1, 0)
        GPIO.output(env.GREEN_1, 1)
        GPIO.output(env.RED_1, 0)
    if index == 2:
        GPIO.output(env.YELLOW_2, 0)
        GPIO.output(env.GREEN_2, 1)
        GPIO.output(env.RED_2, 0)

def onEmer(time_emer):
    timeDown = time_emer
    while timeDown >= 0:
        GPIO.output(env.YELLOW_1, 1)
        GPIO.output(env.YELLOW_2, 1)
        GPIO.output(env.GREEN_1, 0)
        GPIO.output(env.RED_1, 0)
        GPIO.output(env.GREEN_2, 0)
        GPIO.output(env.RED_2, 0)

        time.sleep(1)
        GPIO.output(env.YELLOW_1, 0)
        GPIO.output(env.YELLOW_2, 0)
        time.sleep(0.5)
        timeDown -= 1

def readButton(emer_sate):
    while True:
        api.call()
        state = GPIO.input(env.Button)  
        if state == 1:
            emer_sate[0] = True
        else:
            emer_sate[0] = False
        # print("Trang thai: ", emer_sate)
        
        time.sleep(0.5)

def handelEmer(state):
    if state:
        lcd.lcd_warning_emer()
        seg.off_led()
        onEmer(env.TIME_EMER[0])
        lcd.lcd_init()