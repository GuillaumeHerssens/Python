from datetime import timedelta
from datetime import datetime

def delta(birthday):
    birthday = datetime.strptime(birthday, "%Y/%m/%d %H:%M:%S")
    print (birthday + timedelta(seconds=10e8))

delta("1990/05/18 03:30:00")