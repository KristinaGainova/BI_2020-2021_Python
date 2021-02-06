import numpy as np
import time
import matplotlib.pyplot as plt


def shuffle(l):
    shuffled_list = np.random.permutation(numbers)
    return shuffled_list

def check_sorted(l):
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def monkey_sort(l):
    while not check_sorted(l):
        l = shuffle(l)
    return l


sort_count = 5
lst_max_size = 11

mean_list = []
dispersion_list = []

for list_length in range(0, lst_max_size):
    numbers = np.random.permutation(list_length)
    time_list = []
    for i in range(0, sort_count):
        start = time.perf_counter()
        monkey_sort(numbers)
        end = time.perf_counter()
        time_list.append(end - start)
    mean_time = sum(time_list) / len(time_list)
    dispersion_time = (sum([(x - mean_time) ** 2 for x in time_list]) / len(time_list)) ** 0.5
    mean_list.append(mean_time)
    dispersion_list.append(dispersion_time)
    print(list_length, mean_time, dispersion_time)

list_size = range(0,lst_max_size)
fig,ax = plt.subplots()
plt.xlabel('Size of the list')
plt.ylabel('Time')
plt.title('Monkey sorting: mean and dispersion time calculation')
ax.plot(list_size, mean_list, label = 'Mean time')
ax.plot(list_size, dispersion_list, label = 'Dispersion time')
leg = ax.legend()
plt.show()