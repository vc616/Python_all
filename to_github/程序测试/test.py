import time
from datetime import datetime

while 1 :
    localtime = time.localtime(time.time())
    print(localtime.tm_hour,":",localtime.tm_min,end = "  ")
    time.sleep(3)