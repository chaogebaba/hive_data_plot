from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

csvList = list(Path('.').glob("*.CSV"))
csvList.sort()
print(csvList)

dates, humis, temps, pass_times = [], [], [], []
for File in csvList:
    with open(File) as f:
        reader = csv.reader(f)
        for row in reader:
            curr_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            dates.append(curr_time)
            humis.append(float(row[1]))
            temps.append(float(row[2]))
            pass_times.append(int(row[3]))

fig, ax = plt.subplots()
ax.plot(dates, humis, c="blue", label="Humi")
ax.plot(dates, temps, c="red", label="Temp")
ax.plot(dates, pass_times, c="black", label="Freq")

plt.title("Hive humidity(%), temperature(°C) and hive entrance pass frequency(times)")
fig.autofmt_xdate()
# ax.tick_params(axis="both", which="major", labelsize=10)
# ax.set_ylim([0, 100])
plt.legend(loc="best")
plt.show()
