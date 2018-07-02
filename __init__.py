from Functions import eia860,eia923

print("Begining eia923 imports from years 1970+")
try :
    eia923()
except Exception:
    print("Database is up to date")

print("Begining eia860 imports from years 1990+")
try :
    eia860()
except Exception:
    print("Database is up to date")
    