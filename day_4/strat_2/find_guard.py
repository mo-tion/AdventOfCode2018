from datetime import datetime
import numpy as np

with open("records.txt", "r") as freq_file:
    content = freq_file.readlines()

date_records = []
for record in content:
    date, rest = record.split(']')
    datetime_object = datetime.strptime(date[1:], '%Y-%m-%d %H:%M')
    #print (datetime_object)
    date_records.append((datetime_object, rest[:-1]))

date_records.sort(key = lambda x: x[0])

guard_to_sleep_time = {}

guard_id = -1
sleep_start = None
sleep_end = None
for date, record in date_records:
    if "Guard" in record:
        guard_id = int(record.split(' ')[2][1:])
    if "asleep" in record:
        sleep_start = date
    if "wakes" in record:
        sleep_end = date
        if guard_id > 0 and sleep_end is not None and sleep_start is not None:
            if not guard_id in guard_to_sleep_time:
                guard_to_sleep_time[guard_id] = np.zeros(61)
                guard_to_sleep_time[guard_id] [-1] = 1
            else:
                guard_to_sleep_time[guard_id] [-1] += 1
            for i in range(int(sleep_start.isoformat().split(':')[1]), int(sleep_end.isoformat().split(':')[1])):
                    guard_to_sleep_time[guard_id] [i] += 1

max_sleep = -1
max_id = -1
max_min = -1
for guard_id, sleep_record in guard_to_sleep_time.iteritems():
    sleep_time = np.max(sleep_record[:-1])
    if sleep_time > max_sleep:
        max_sleep = sleep_time
        max_id = guard_id
        max_min = np.argmax(sleep_record[:-1])

print(max_min*max_id)
