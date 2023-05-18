from datetime import *;
from dateutil.relativedelta import *
# import calendar

NOW = datetime.now()
TODAY = date.today()

# Next month, plus one week, at 10am.
TODAY+relativedelta(months=+1, weeks=+1, hour=10)