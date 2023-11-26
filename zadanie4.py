import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Создаем данные для графика
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2 * x)

# Создаем окно для задания исходных волн
fig, ax = plt.subplots(3, 1, figsize=(8, 6))

# Первое интерактивное окно для задания первой волны
ax[0].plot(x, y1)
ax[0].set_title('Исходная волна 1')

# Второе интерактивное окно для задания второй волны
ax[1].plot(x, y2)
ax[1].set_title('Исходная волна 2')

# Окно для отображения результата сложения волн
ax[2].set_title('Результат сложения волн')


# Функция для обновления графика при изменении параметров волн
def update(val):
    amp1 = amp_slider1.val
    freq1 = freq_slider1.val
    amp2 = amp_slider2.val
    freq2 = freq_slider2.val

    y_result = amp1 * np.sin(freq1 * x) + amp2 * np.sin(freq2 * x)

    ax[2].clear()
    ax[2].plot(x, y_result)
    ax[2].set_title('Результат сложения волн')


# Добавляем слайдеры для регулировки параметров волн
amp_slider1_ax = fig.add_axes([0.1, 0.05, 0.65, 0.03])
amp_slider1 = Slider(amp_slider1_ax, 'Амплитуда 1', 0.1, 1.0, valinit=1)
amp_slider1.on_changed(update)

freq_slider1_ax = fig.add_axes([0.1, 0.01, 0.65, 0.03])
freq_slider1 = Slider(freq_slider1_ax, 'Частота 1', 0.1, 10.0, valinit=1)
freq_slider1.on_changed(update)

amp_slider2_ax = fig.add_axes([0.1, 0.9, 0.65, 0.03])
amp_slider2 = Slider(amp_slider2_ax, 'Амплитуда 2', 0.1, 1.0, valinit=1)
amp_slider2.on_changed(update)

freq_slider2_ax = fig.add_axes([0.1, 0.94, 0.65, 0.03])
freq_slider2 = Slider(freq_slider2_ax, 'Частота 2', 0.1, 10.0, valinit=2)
freq_slider2.on_changed(update)

plt.show()
