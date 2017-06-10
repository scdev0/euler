def counting_sundays(start_year, end_year, first_sunday):
    '''Return the number of Sundays that fall on the first on the month from start-year to end_year.
    >>> counting_sundays(2016, 2016, 3)
    1
    >>> counting_sundays(2016, 2017, 3)
    3
    '''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = first_sunday
    count = 0
    for year in range(start_year, end_year+1):
        for month in range(0, 12):
            if day == 1:
                count += 1
            if year % 4 == 0 and month == 1: # leap year and Feb
                while day < (month_days[month]+1):
                    day += 7
                day = day % (month_days[month] + 1)
            else:
                while day < month_days[month]:
                    day += 7                
                day = day % month_days[month]
    return count

# using datetime module
import datetime
def counting_sundays2(start_year, end_year):
    '''Return the number of Sundays that fall on the first on the month from start-year to end_year.
    >>> counting_sundays2(2016, 2016)
    1
    >>> counting_sundays2(2016, 2017)
    3
    '''    
    count = 0
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                count += 1
    return count
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(counting_sundays(1901, 2000, 6))
    print(counting_sundays2(1901, 2000))