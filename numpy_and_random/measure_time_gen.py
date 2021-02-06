import random
import numpy as np
import time
import matplotlib.pyplot as plt
amount_numbers = range(0, 1001)
time_random = []
time_numpy = []
time_numpy_size = []


for i in range(0, 1001):
    random_time_begin = time.perf_counter()
    for j in range(0, i):
        random.random()
    random_time_end = time.perf_counter()
    time_random.append(random_time_end - random_time_begin)

    numpy_time_begin = time.perf_counter()
    for j in range(0, i):
        np.random.random()
    numpy_time_end = time.perf_counter()
    time_numpy.append(numpy_time_end - numpy_time_begin)

    numpy_size_time_begin = time.perf_counter()
    np.random.random(i)
    numpy_size_time_end = time.perf_counter()
    time_numpy_size.append(numpy_size_time_end - numpy_size_time_begin)

fig,ax = plt.subplots()
plt.xlabel('Amount of numbers between 0 to 1 which were generated')
plt.ylabel('Time')
plt.title('Time calculation of random numbers')
ax.plot(amount_numbers,time_random, label = 'Time with random module')
ax.plot(amount_numbers,time_numpy, label = 'Time with numpy module')
ax.plot(amount_numbers,time_numpy_size, label = 'Time with numpy module and size argument')
leg = ax.legend()
plt.show()