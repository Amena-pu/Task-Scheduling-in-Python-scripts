import schedule
import time
import os
def note():
       os.system("C:\\Windows\\notepad.exe")

schedule.every().thursday.at("11:06").do(note)
while True:
    schedule.run_pending()
    time.sleep(1)