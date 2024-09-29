import datetime
import calendar

def day_of_week(day,month,year):
    week_days = ['Понедельник','Вторник', 'Среда','Четверг','Пятница','Суббота','Воскресенье']
    target_date = datetime.datetime(year,month,day)
    day_idx = target_date.weekday()
    return week_days[day_idx]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year

day = int(input("Введите день вашего рождения:"))
month = int(input("введите месяц вашего рождения:"))
year = int(input("Введите год вашего рождения:"))

day_of_week_result = day_of_week(day,month,year)
print(f"Это был день недели:{day_of_week_result}")

leap_year_result=is_leap_year(year)
if leap_year_result:
    print("Это был високосный год.")
else:
    print("Это был не високосный год.")
    
age = calculate_age(year)
print(f"Вам сейчас {age} лет.")

print(f"Дата вашего рождения: {str(day).rjust(2,'*')} {str(month).rjust(2,'*')} {str(year).rjust(4,'*')}")
