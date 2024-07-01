from workalendar.america.brazil import BrazilBankCalendar
from datetime import datetime

d = datetime(2023, 9, 15)

calendar = BrazilBankCalendar()
d1 = calendar.add_working_days(d, 1)
print(d1)