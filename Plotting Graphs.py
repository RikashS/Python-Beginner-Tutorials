import matplotlib.pyplot as plt
# x = [1, 3, 5, 10]
# plt.plot(x)
# plt.show()
# y = [7, 12, 21, 22]
# plt.plot(x, y)
# plt.show()

x = [3, 9, 14]
y = [2, 7, 30]
plt.plot(x, y, c="red", linewidth=2, label="line 1")
# Plotting x2 and y2
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c="green", linewidth=2, label="line 2", linestyle="dashed",
         marker='s', markerfacecolor="orange", markersize=10)

# # label the axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Lines!")

plt.ylim(1, 10)
plt.xlim(0, 30)
# # Show the legend on the plot
plt.legend()
# # Get Python to show the plot
plt.show()