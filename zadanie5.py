import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Создаем данные для графика
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(2*np.pi*X) * np.cos(2*np.pi*Y)

# Создаем первый график
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('График функции')

# Создаем второй график
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_yscale('log')
ax2.set_title('График функции в логарифмическом масштабе по оси Y')

# Отображаем графики
plt.show()