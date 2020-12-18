import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_TimeAverage(x :list, y :list, file_name :str):
    times = x
    n_result = y

    time_average = []
    sum_t = 0
    for num in n_result:
        sum_t += num
        time_average.append(sum_t)

    for i in range(len(times)):
        if times[i] == 0:
            continue
        time_average[i] /= times[i]

    plt.figure()
    plt.plot(times, time_average)
    plt.xlabel("t")
    plt.ylabel("time_average")
    plt.savefig(file_name)

Output = pd.read_csv("./a_output.csv")

Output.set_index('ncum', inplace=True)
print(Output)

columns = Output.columns.values
print(columns)

col_x = Output["t"]
col_y = Output["n(t)"]

plt.plot(col_x, col_y)

# n(t)に対して回帰直線を引く
## x, y軸を成形
x = col_x.to_numpy()
y = col_y.to_numpy()
x = x.reshape(-1,1)
y = y.reshape(-1,1)
## 線形回帰
mod = LinearRegression()
mod_lin = mod.fit(x, y)
y_lin_fit = mod_lin.predict(x)
plt.plot(x, y_lin_fit, color = 'r', linewidth=1.5)

plt.xlabel("t")
plt.ylabel("n(t)")
plt.savefig("./PlotCSV.png")

plot_TimeAverage(col_x.tolist(), col_y.tolist(), "./PlotCSV2.png")
