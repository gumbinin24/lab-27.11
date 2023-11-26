import numpy as np
from scipy.special import legendre
import matplotlib.pyplot as plt


def plot_legendre(n):

    # Создаем массив значений x от -1 до 1
    x = np.linspace(-1, 1, 100)

    # Вычисляем значения полинома Лежандра заданной степени
    P = legendre(n)(x)

    # Отрисовываем график
    plt.plot(x, P, label=f"n = {n}")

    # Добавляем легенду
    plt.legend()

    # Добавляем заголовок
    plt.title("Полиномы Лежандра")

    # Отображаем график
    plt.show()


# Цикл значений
for n in range(1, 8):
    plot_legendre(n)
