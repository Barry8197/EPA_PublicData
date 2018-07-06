import getpass
import os
import sys


username = getpass.getuser()
os.chdir('/Users/%s/EPA_PublicData' % (username))
location = os.getcwd()
file_name = "__init__.cron"
output = open(file_name, 'w')
output.write("*/2 * * * * ")
path = 'cd %s ;' % (location)
output.write(path)
output.write(sys.executable)
output.write(" __init__.py")
output.write("\n")
output.close()


os.system('crontab __init__.cron ')