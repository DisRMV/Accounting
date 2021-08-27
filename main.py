from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.today().date())
    print(get_employees())
    print(calculate_salary())
