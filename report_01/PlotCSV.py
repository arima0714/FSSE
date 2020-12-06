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
