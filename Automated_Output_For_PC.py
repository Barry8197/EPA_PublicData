import getpass
import os
import sys

username = getpass.getuser()
os.system('SCHTASKS /Create /SC MONTHLY /MO first /D MON /TN Update_PSQL /TR c:\\Users\\%s\\EPA_PublicData' %(username))
