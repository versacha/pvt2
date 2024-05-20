import matplotlib.pyplot as plt

times = {
    15000: [0.405004, 0.299761, 0.232367, 0.198480],
    20000: [0.944678, 0.515416, 0.488715, 0.444752],
    25000: [59.225132, 42.981681, 46.982656, 45.879530]
}

threads = [2, 4, 6, 8]

def calculate_speedup(times):
    speedup = []
    for n, t in times.items():
        t1 = t[0]
        s = [t1 / ti for ti in t]
        speedup.append(s)
    return speedup

speedup = calculate_speedup(times)

fig, ax = plt.subplots()

for i, n in enumerate(times.keys()):
    ax.plot(threads, speedup[i], marker='o', label=f'n = m = {n}')

ax.set_xlabel('Число потоков (P)')
ax.set_ylabel('Коэффициент ускорения (S)')
ax.set_title('Зависимость коэффициента ускорения от числа потоков')
ax.legend()
ax.grid(True)

plt.savefig('график.png')
plt.show()