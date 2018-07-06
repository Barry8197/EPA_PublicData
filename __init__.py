from Functions import eia860,eia923
import warnings
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def scheduled_func()
    print("Begining eia923 imports from years 1970+")
    try :
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            eia923()

    except Exception:
        print("Database is up to date")

    print("Begining eia860 imports from years 1990+")
    try :
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            eia860()

    except Exception:
        print("Database is up to date")
    
    
scheduler.add_job(scheduled_func, 'interval', minutes = 1, id='my_job_id')
scheduler.start()
