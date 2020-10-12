import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

infile = open("DATALOG2.csv", "r")


File = pd.read_csv(infile, names=("height", "xG", "yG", "zG", "time"), sep=";")
length = len(File)

print(File)
print(np.max(File["time"]))

plt.plot(File["time"] / 1000, File["xG"], label="xG")
plt.plot(File["time"] / 1000, File["yG"], label="yG")
plt.plot(File["time"] / 1000, File["zG"], label="zG")
plt.legend()
plt.show()

plt.plot(File["time"] / 1000, File["height"], label="Height (m)")
plt.legend()
plt.show()
