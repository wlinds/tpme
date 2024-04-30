from utils.utils import generate_datetime
import numpy as np
from datetime import datetime, timedelta
from main import gen_name

def generate_time_reports(num_people=4, shift_length=4):
    time_reports = {}

    for i in range(1, num_people + 1):
        person_name = gen_name()
        num_reports = np.random.randint(5, 10)

        reports = []
        for _ in range(num_reports):
            start_time = generate_datetime()
            end_time = (datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=shift_length)).strftime('%Y-%m-%d %H:%M:%S')
            reports.append({"start_time": start_time, "end_time": end_time})

        time_reports[person_name] = reports

    return time_reports

if __name__ == "__main__":
    print(generate_time_reports())