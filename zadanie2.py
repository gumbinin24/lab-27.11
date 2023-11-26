import numpy as np
import matplotlib.pyplot as plt


def plot_lissajous(freq_ratio):
    # Создаем массив значений t от 0 до 2*pi
    t = np.linspace(0, 2 * np.pi, 1000)

    # Вычисляем значения x и y для первого колебания
    x1 = np.sin(3 * t)
    y1 = np.cos(2 * t)

    # Вычисляем значения x и y для второго колебания
    x2 = np.sin(3 * t)
    y2 = np.cos(freq_ratio * 2 * t)

    # Отрисовываем график
    plt.plot(x1, y1, label="Первое колебание")
    plt.plot(x2, y2, label="Второе колебание")

    # Добавляем легенду
    plt.legend()

    # Добавляем заголовок
    plt.title(f"Фигура Лисажу с соотношением частот {freq_ratio}")

    # Отображаем график
    plt.show()


plot_lissajous(3/2)
plot_lissajous(3/4)
plot_lissajous(5/4)
plot_lissajous(5/6)
