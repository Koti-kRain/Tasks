import datetime
import calendar


def get_birthday():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return day, month, year

def day_of_week(day, month, year):
    week_days = ['Понедельник','Вторник', 'Среда','Четверг','Пятница','Суббота','Воскресенье']
    target_date = datetime.datetime(year,month,day)
    day_idx = target_date.weekday()
    return week_days[day_idx]

def is_leap_year(year):
    return calendar.isleap(year)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def display_date_as_stars(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    date_str = f"{day_str} {month_str} {year_str}"
    print((date_str))

def main():
    day, month, year = get_birthday()
    print(f"Это был день недели {day_of_week(day, month, year)}.")
    print(f"Это был {'високосный' if is_leap_year(year) else 'не високосный'} год.")
    print(f"Вам сейчас {calculate_age(day, month, year)} лет.")
    print("Ваша дата рождения в формате ** ** ****:")
    display_date_as_stars(day, month, year)

if __name__ == "__main__":
    main()
