import application.salary as salary
import application.db.people as people
# import application.db
from datetime import datetime
def get_current_date():
    current_datetime = datetime.now()
    current_date = str(datetime.date(current_datetime))
    PATTERN_IN = "%Y-%m-%d"
    PATTERN_OUT = "%d-%m-%Y"
    date_formatting = datetime.strptime(current_date, PATTERN_IN)
    print(datetime.strftime(date_formatting, PATTERN_OUT))
if __name__ == '__main__':
    while True:
        command = input('Введите команду s/e (q - выход): ')
        if command == 's':
            salary.calculate_salary()
            get_current_date()
        if command == 'e':
            people.get_employees()
            get_current_date()
        if command == 'q':
            break