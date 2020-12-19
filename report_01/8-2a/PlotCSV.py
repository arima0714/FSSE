import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

Output = pd.read_csv("./a_output.csv")

Output.set_index('ncum', inplace=True)
print(Output)

columns = Output.columns.values
print(columns)

col_x = Output["t"]
col_y = Output["E"]

plt.plot(col_x, col_y)

# Eに対して回帰直線を引く
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
plt.ylabel("all energy")
plt.savefig("./PlotCSV.png")
