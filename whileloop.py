# exponential backoff 

import time

waittime = 1.0
 
maxretries = 5
attempts = 0

while attempts < maxretries:
    print("attempts" ,attempts + 1 , "wait time", waittime, flush = True) # flush=True forces the terminal to display the line immediately before sleeping
    time.sleep(waittime)
    waittime *=2
    attempts +=1
print("Max retries reached or process completed.") # run 5 times and then this code execute