from datetime import *
from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(datetime.today().date())
    print(get_employees())
    print(calculate_salary())
