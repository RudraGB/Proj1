
import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split(" "))
    weekday = calendar.weekday(year,month,day)
    print(weekday)
    print(calendar.day_name[weekday].upper())

