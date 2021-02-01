import matplotlib.pyplot as plt
# Prepare data
x = [1, 5, 10, 15, 20]
y1 = [4, 16, 4, 8, 17]
y2 = [12, 14, 10, 12, 5]

plt.figure(figsize=(12, 7))
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.plot(x, y2, 's-c', label="second", mec='b', lw=2, mew=2, ms=10)
plt.plot(x, y1, '-.k', marker="o", label="first", lw=3, mec='r', mew=2, ms=10)
plt.gca().legend(loc='upper right',  bbox_to_anchor=(1, 0.5))
axes = plt.gca()
axes.xaxis.label.set_size(20)
axes.yaxis.label.set_size(20)
plt.grid(True)
plt.savefig('C:/bioinformatics_institute/python/line_plot.png')
plt.show()
