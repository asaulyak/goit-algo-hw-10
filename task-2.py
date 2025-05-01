import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def is_inside(x, y):
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    average_area = 0

    for _ in range(num_experiments):
        points = [(random.uniform(0, b - a), random.uniform(0, f(b))) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * ((b - a) * f(b))

        # Додавання до середньої площі
        average_area += area

        # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


# Обчислення інтеграла
result, error = spi.quad(f, a, b)

monte_carlo_area = monte_carlo_simulation(a, b, 100)

print("Інтеграл: ", result, error)
print("Інтеграл monte carlo: ", monte_carlo_area)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
