import matplotlib.pyplot as plt

x1 = [2, 4, 10, 9, 10, 3]
y1 = [12, 5, 7, 6, 11, 13]

x2 = [1, 9, 6, 4, 3, 5]
y2 = [3, 4, 9, 5, 1, 7]

plt.plot(x1, y1,linestyle= 'dotted')
plt.plot(x2, y2,linestyle= 'solid')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("TEST", size=20, color='Blue')

plt.show()

