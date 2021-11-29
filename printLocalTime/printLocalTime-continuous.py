import datetime
import time

from os import close

numExecutions = 1
while(True):
    print("Successfully executed %d times at " % numExecutions, datetime.datetime.now())
    numExecutions+=1
    time.sleep(300)
