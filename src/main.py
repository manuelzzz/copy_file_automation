import os
from copy_files import copy
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
load_dotenv()

copy_hour = os.getenv('COPY_HOUR')
file_path = os.getenv('FILE_PATH')
file_destination = os.getenv('FILE_DESTINATION')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=copy_hour)
def copy_job():
    copy(file_path=file_path, file_destination=file_destination)
    print("copia arquivo")


sched.start()
