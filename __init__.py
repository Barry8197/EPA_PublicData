from Functions import eia860,eia923
import warnings
from Constants import Years_eia860, Years_eia923
import os
import shutil
import datetime

now = datetime.datetime.now()
file_name = "Automated_Output.txt"
output = open(file_name, 'a')

path = os.getcwd()
try :
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        eia923()
        output.write("\n")

except Exception:
    output.write("")

os.chdir(path)
try :
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        eia860()
        output.write("Database is up to date\n")

except Exception:
    output.write("Database is up to date\n")


try :
    for year1,year2 in zip(Years_eia860,Years_eia923):
        os.chdir(path)
        shutil.rmtree("%s/%s" % (path,year1))
        shutil.rmtree("%s/%s" % (path,year2))

except Exception :
    output.write("")
    
output.write("The database was last updated on the %s-%s-%s at %2i:%2i \n" % (now.month, now.day,now.year, now.hour,now.minute))
output.write("\n")