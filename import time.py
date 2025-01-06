import time
import os

while True:
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S" , current_time)
    os.system('clear')
    print(formatted_time)
    time.sleep(1)