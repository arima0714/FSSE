import pandas as pd
import matplotlib.pyplot as plt

Output = pd.read_csv("./a_output.csv")

Output.set_index('ncum', inplace=True)
print(Output)

columns = Output.columns.values
print(columns)
X = columns[0]
Y = columns[1]

col_x = Output[X]
col_y = Output[Y]

plt.plot(col_x, col_y)
plt.savefig("./PlotCSV.png")
