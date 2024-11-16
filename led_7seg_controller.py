import variableAndContrants as env
import threading as cpu
from EmulatorGUI import GPIO
import time

# bit 0 sẽ là bật đèn do chung Anote
# sap xem theo A B C D E F G
map_digital = [
    [0, 0, 0, 0, 0, 0, 1],  # hiển thị số 0
    [1, 0, 0, 1, 1, 1, 1],  # hiển thị số 1
    [0, 0, 1, 0, 0, 1, 0],  # hiển thị số 2
    [0, 0, 0, 0, 1, 1, 0],  # hiển thị số 3
    [1, 0, 0, 1, 1, 0, 0],  # hiển thị số 4
    [0, 1, 0, 0, 1, 0, 0],  # hiển thị số 5
    [0, 1, 0, 0, 0, 0, 0],  # hiển thị số 6
    [0, 0, 0, 1, 1, 1, 1],  # hiển thị số 7
    [0, 0, 0, 0, 0, 0, 0],  # hiển thị số 8
    [0, 0, 0, 0, 1, 0, 0],  # hiển thị số 9
]

def count_down(color):
    if color == env.GREEN_1:
        time_down = env.TIME_GREEN[0]
        while time_down >= 1:
            print(f"Đèn xanh 1 còn lại: {time_down} giây")  # In ra thời gian còn lại của đèn xanh 1
            time_led_2 = time_down + env.TIME_YELLOW[0]
            print(f"Đèn đỏ 2 còn lại: {time_led_2} giây")
            print("------------------------------------")
            handle_concurrent(time_down, time_down + env.TIME_YELLOW[0])
            time_down -= 1
            time_led_2 -= 1

    if color == env.YELLOW_1:
        time_down = env.TIME_YELLOW[0]
        while time_down >= 1:
            print(f"Đèn vàng 1 còn lại: {time_down} giây")  # In ra thời gian còn lại của đèn vàng
            print(f"Đèn đỏ 2 còn lại: {time_down} giây")
            print("------------------------------------")
            handle_concurrent(time_down, time_down)
            time_down -= 1

    if color == env.YELLOW_2:
        time_down = env.TIME_YELLOW[0]
        while time_down >= 1:
            print(f"Đèn vàng 2 còn lại: {time_down} giây")  # In ra thời gian còn lại của đèn vàng
            print(f"Đèn đỏ 1 còn lại: {time_down} giây")
            print("------------------------------------")
            handle_concurrent(time_down, time_down)
            time_down -= 1

    if color == env.GREEN_2:
        time_down = env.TIME_GREEN[0]
        while time_down >= 1:
            print(f"Đèn xanh 2 còn lại: {time_down} giây")  # In ra thời gian còn lại của đèn xanh 2
            time_led_1 = time_down + env.TIME_YELLOW[0]
            print(f"Đèn đỏ 1 còn lại: {time_led_1} giây")
            print("------------------------------------")
            handle_concurrent(time_down + env.TIME_YELLOW[0], time_down)
            time_down -= 1
            time_led_1 -= 1


def handle_concurrent(time_led_1, time_led_2):
    break_time = [1]
    theard_7seg = cpu.Thread(target=interup, args=(break_time,))
    theard_7seg.start()
    
    while break_time[0]:
        push8bit(time_led_1)
        GPIO.output(env.LED_PIN_D1, 1)  
        time.sleep(0.005)
        GPIO.output(env.LED_PIN_D1, 0)

        push8bit(time_led_2)
        GPIO.output(env.LED_PIN_D2, 1)  
        time.sleep(0.005)
        GPIO.output(env.LED_PIN_D2, 0)

def interup(break_time):
    time.sleep(1)  # đặt tốc độ đếm 1s
    break_time[0] = 0

def push8bit(led_num):
    temp = map_digital[led_num]

    for index, val in enumerate(temp):
        GPIO.output(env.LED_7segs[index], val)  

def off_led():
    GPIO.output(env.LED_PIN_D1, 0)  
    GPIO.output(env.LED_PIN_D2, 0)  