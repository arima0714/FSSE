import pandas as pd
import matplotlib.pyplot as plt

EulerRichardsonOutput = pd.read_csv("./Output.txt")

print(EulerRichardsonOutput)

columns = EulerRichardsonOutput.columns.values
print(columns)
X = columns[0]
Y = columns[1]

col_x = EulerRichardsonOutput[X]
col_y = EulerRichardsonOutput[Y]

plt.plot(col_x, col_y)
plt.savefig("./PlotCSV.png")

# E/m(=全エネルギー)のプロットを行う
E_per_m = EulerRichardsonOutput[columns[2]]

time = []
time_sum = 0
dt = 0.01
for i in range(len(E_per_m)):
    time.append(time_sum)
    time_sum += dt

plt.figure()
plt.plot(time, E_per_m)
plt.savefig("./Plot_E_per_m.png")

print(f"len(time) = {len(time)}, len(E_per_m) = {len(E_per_m)}")
