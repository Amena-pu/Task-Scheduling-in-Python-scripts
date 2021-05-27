import schedule
import time

def job():
    print("I am doing this job!")



schedule.every().thursday.at("07:38").do(job)


while True:
    schedule.run_pending()
    time.sleep(1) 