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
    sum_t == num
    time_average.append(sum_t)
