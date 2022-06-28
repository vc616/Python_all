import time
while 1:
    if int(time.time()) % 60 == 0:
        print(time.time())
    time.sleep(1)