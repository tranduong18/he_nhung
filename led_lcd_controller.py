import variableAndContrants as env
import time
from EmulatorGUI import GPIO

LCD_WIDTH = 16   

def lcd_init():
    # Khởi tạo hiển thị
    print("Khởi tạo hiển thị")
    lcd_string("Traffic LCD    <", 1)
    lcd_string("Den Giao thong <", 2)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    print(f"Đã hiển thị: '{message}' trên dòng {line}")
    print("----------------------------------------")

def lcd_warning_emer():
    lcd_string("Traffic LCD    <", 1)
    lcd_string("Den Uu Tien    <", 2)

def lcd_night_mod():
    lcd_string("Traffic LCD    <", 1)
    lcd_string("Buoi toi       <", 2)

def lcd_toggle_enable():
    time.sleep(E_DELAY)
    print("Bật hiển thị")

def lcd_clear():
    print("Xóa màn hình LCD")