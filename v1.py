# this only works for year 2000 to 2099


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def year_code(self):
        year = int(str(self.year)[-2:])
        code = (year + (year // 4)) % 7
        return code

    def month_code(self):
        code = {1: 6, 2: 2, 3: 2,  4: 5,  5: 0,  6: 3,
                7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4, }
        if self.year % 4 == 0:
            code[1] = 5
            code[2] = 1
        return code[self.month]

    def the_day(self):
        days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday', 0: 'Sunday', }
        a = (self.month_code() + self.day + self.year_code()) % 7
        return days[a]


d1 = Date(25, 12, 2023)
print(d1.the_day())
