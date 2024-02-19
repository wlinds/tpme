from utils.utils import generate_datetime
import numpy as np
from main import gen_name

def generate_time_reports(num_people=4):
    time_reports = {}

    for i in range(1, num_people + 1):
        person_name = gen_name()
        num_reports = np.random.randint(5, 10)

        reports = [generate_datetime() for _ in range(num_reports)]
        time_reports[person_name] = reports

    return time_reports

if __name__ == "__main__":
    print(generate_time_reports())