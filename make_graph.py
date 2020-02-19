import matplotlib.pyplot as plt
import numpy as np
import math, random

def lineplot(x_data, y_data, modes, median, average, x_label="", y_label="", title=""):

    _, ax = plt.subplots()

    ax.plot(x_data, y_data, lw = 1, color = '#000000', alpha = 1)

    ax.grid()

    for mode in modes:
        ax.vlines(mode[0], 0, mode[1], color = '#000000', linestyle = ':')
    
    ax.vlines(median[0], 0, median[1], color = '#000000', linestyle = '--')

    ax.vlines(average[0], 0, average[1], color = '#000000', linestyle = '-')

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()

data = sorted(list(map(int, input("Enter your data: ").split())))
# data = []

# for i in range(1000):
#     data.append(random.randint(0, 50))

# data = sorted(data)

distribution_dict = {}

for el in data:
    if (el not in distribution_dict):
        distribution_dict[el] = 1
    else:
        distribution_dict[el] += 1

print("Distribution table: ", distribution_dict)

graph_dataX = []
graph_dataM = []

for el in distribution_dict:
    graph_dataX.append(el)
    graph_dataM.append(distribution_dict[el])

modes = []

for elIndex in range(len(sorted(graph_dataM)[:: -1])):
    if (graph_dataM[elIndex] == max(graph_dataM)):
        modes.append((graph_dataX[elIndex], graph_dataM[elIndex]))

median = 0

if (len(data) % 2 != 0):
    median = (data[len(data) // 2], distribution_dict[data[len(data) // 2 - 1]])
else:
    median = ((data[len(data) // 2 - 1] + data[len(data) // 2]) / 2, (distribution_dict[math.floor((data[len(data) // 2 - 1] + data[len(data) // 2]) / 2)] + distribution_dict[math.ceil((data[len(data) // 2 - 1] + data[len(data) // 2]) / 2)]) / 2)

average = [0, 0]

for el in data:
    average[0] += el

average[0] /= len(data)
average[1] = (distribution_dict[math.floor(average[0])] + distribution_dict[math.ceil(average[0])]) / 2

print("Median: ", median)

print("Average: ", average)

print("Modes: ", modes)

lineplot(graph_dataX, graph_dataM, modes, median, average, "X", "M", "Frequency range")

input()