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
output.write("Beginning eia923 imports from years 1970+\n")
output.write("Fetching data for years...\n")
output.close()
output = open(file_name, 'a')
for year in Years_eia923:
    os.chdir(path)
    try :
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            eia923(year)

    except Exception:
        output.write("")

output.write("Eia923 database is up to date \n \n")

for year in Years_eia923:
    try:
        os.chdir(path)
        shutil.rmtree("%s/%s" % (path,year))

    except Exception:
        output.write("")
    
output.close()
os.chdir(path)
output = open(file_name, 'a')

output.write("Beginning eia860 imports from years 1990+\n")
output.write("Fetching data for years...\n")
output.close()
output = open(file_name, 'a')
for year in Years_eia860:
    os.chdir(path)
    try :
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            eia860(year)

    except Exception:
        output.write("")

output.write("Eia860 database is up to date \n \n")
    
for year in Years_eia860:
    try:
        os.chdir(path)
        shutil.rmtree("%s/%s" % (path,year))

    except Exception:
        output.write("")
    
output.write("The database was last updated on the %s-%s-%s at %2i:%2i \n" % (now.month, now.day,now.year, now.hour,now.minute))
output.write("\n")
output.close()