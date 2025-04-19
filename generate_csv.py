import csv
import datetime
import random

initial_date = datetime.datetime(2025, 1, 1, 0, 0, 0)
data = []
for _ in range(30):
    delta_seconds = random.uniform(0, 10)
    initial_date = initial_date + datetime.timedelta(seconds=delta_seconds)
    d = f'This is a useless data, with a random number: {random.randint(100, 999)}'
    data.append((initial_date.isoformat(), d))
data.sort()
with open("random_data.csv", mode="w", newline="") as timestamped_data:
    writer = csv.writer(timestamped_data)
    writer.writerow(["timestamp", "value"]) 
    writer.writerows(data)
print("OK")
