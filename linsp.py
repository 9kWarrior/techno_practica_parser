import matplotlib.pyplot as plt

# Ваши неотсортированные данные
x = [3, 1, 4, 2]
y = [5, 2, 7, 1]

# Отсортированные данные по оси X
sorted_x, sorted_y = zip(*sorted(zip(x, y)))

# Построение графика
plt.plot(sorted_x, sorted_y)

# Отображение графика
plt.show()