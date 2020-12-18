import pandas as pd
import matplotlib.pyplot as plt

Output = pd.read_csv("./a_output.csv")

Output.set_index('ncum', inplace=True)
print(Output)

columns = Output.columns.values
print(columns)

col_x = Output["t"]
col_y = Output["n(t)"]

plt.plot(col_x, col_y)
plt.xlabel("t")
plt.ylabel("n(t)")
plt.savefig("./PlotCSV.png")


time_average = []
sum_t = 0
for num in col_y:
    sum_t += num
    time_average.append(sum_t)

print(f"type(time_average) = {type(time_average)}, type(col_x) = {type(col_x)}")
print(f"len(time_average) = {len(time_average)}, len(col_y) = {len(col_x)} ... これらの値が同値であることを期待している")

times = col_x.tolist()

for i in range(len(times)):
    if times[i] == 0:
        continue
    time_average[i] /= times[i]

plt.figure()
plt.plot(times, time_average)
plt.xlabel("t")
plt.ylabel("time_average")
plt.savefig("./PlotCSV2.png")
