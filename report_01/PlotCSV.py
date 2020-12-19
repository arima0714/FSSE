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

# 面積速度のプロットを行う
lr_list = []
lr = 0
def return_deviation_square(num1, num2):
    return( (num1-num2) ** 2)

for i in range(len(col_x) - 1):
    lr = (return_deviation_square(col_x[i], col_x[i+1]) + return_deviation_square(col_y[i], col_y[i+1])) ** 0.5
    lr_list.append(lr)

print(f"len(lr_list) = {len(lr_list)}, len(time) = {len(time[:-1])}")

plt.figure()
plt.plot(time[:-1], lr_list)
plt.savefig("Plot_lr.png")
