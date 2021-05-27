
import schedule
import time
import subprocess

def note():
       subprocess.Popen('C:\\Windows\\System32\\calc.exe')
schedule.every().thursday.at("08:04").do(note)
while True:
    schedule.run_pending()
    time.sleep(1)

