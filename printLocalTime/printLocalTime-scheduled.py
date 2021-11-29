import datetime
import logging
from os import close

# logging.info("hello World")

try:
    f = open("example.txt", "r")
    f.close()
except :
    f = open("example.txt", "w")
    f.write("1")
    f.close()

f = open("example.txt", "r+")
numExecutions = int(f.read())
print("Successfully executed %d times at " % numExecutions, datetime.datetime.now())

numExecutions += 1
f.seek(0)
f.write(str(numExecutions))
f.truncate()

f.close()