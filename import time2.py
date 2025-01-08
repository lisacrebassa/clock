import time
import os

while True:
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S" , current_time)
    # os.system('clear')
    print(current_time, end='\r')
    time.sleep(1)