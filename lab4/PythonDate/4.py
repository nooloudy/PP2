from datetime import datetime
from datetime import time

date1 = datetime.strptime('2020-12-12 12:12:12' , '%Y-%m-%d %H:%M:%S')
datetoday = datetime.now()
result = datetoday - date1
print(result.days * 24 * 3600 + result.seconds)
