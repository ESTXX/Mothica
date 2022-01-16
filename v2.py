# Link for the formula 'https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week/'
# The date from 01/01/0001 to 10/04/1582 is in Julian's calendar.
# Starting October 15, 1582, is in the Gregorian calendar.
import numpy as np


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def century_code(self):
        # julian century code
        ce = (self.year - 1) // 100 + 1  # century
        if self.year in np.arange(100, 1500, 100):
            return (18 - ce) % 7
        elif self.day <= 4 and self.month == 10 and self.year == 1582:
            return (19 - ce) % 7
        elif self.month <= 9 and self.year <= 1582:
            return (19 - ce) % 7
        elif self.year < 1582:
            return (19 - ce) % 7
        # gregorian century code
        i = int(str(self.year)[:2])
        code = ([x for x in np.arange(0, 105, 4) if x > i][0] - 1 - i)*2
        return code

    def month_code(self):
        # month code
        a = {1: 0, 2: 3, 3: 3,  4: 6,  5: 1,  6: 4,
             7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
        # If leap year Subtract one from January and February
        if self.year % 4 == 0:
            a[1] = -1
            a[2] = 2
        return a[self.month]

    def year_code(self):
        b = int(str(self.year)[-2:])
        return b + (b // 4) % 7

    def the_day(self):
        days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                0: 'Sunday', }
        day = (self.century_code() + self.month_code() + self.year_code() + self.day) % 7
        if self.year == 1582 and self.month == 10 and self.day in np.arange(5, 15):
            return None
        return days[day]


Nikola_Tesla = Date(10, 7, 1856)
print(f'10/07/1856 was a {Nikola_Tesla.the_day()}\n')

Thomas_Edison = Date(11, 2, 1847)
print(f'11/02/1847 was a {Thomas_Edison.the_day()}')
