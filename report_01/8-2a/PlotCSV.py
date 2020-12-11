import pandas as pd
import matplotlib.pyplot as plt

Output = pd.read_csv("./a_output.csv")

Output.set_index('ncum', inplace=True)
print(Output)

columns = Output.columns.values
print(columns)

col_x = Output["t"]
col_y = Output["E"]

plt.plot(col_x, col_y)
plt.savefig("./PlotCSV.png")
