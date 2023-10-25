import tkinter as tk
import numpy as np


# Функция для вычисления интерполяционного полинома Лагранжа
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for j in range(n):
        term = y[j]
        for k in range(n):
            if k != j:
                term *= (xi - x[k]) / (x[j] - x[k])
        result += term
    return result


# Функция для отображения интерполяции и координатных плоскостей
def plot_interpolation():
    canvas.delete("all")

    x_values = [float(x_entry.get()) for x_entry in x_entries]
    y_values = [float(y_entry.get()) for y_entry in y_entries]

    # Определение диапазона для построения графика
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)

    # Определение интервала для координатных плоскостей
    x_interval = (x_max - x_min) / 10
    y_interval = (y_max - y_min) / 10

    for xi in np.linspace(x_min, x_max, 400):
        yi = lagrange_interpolation(x_values, y_values, xi)
        x_pixel = (xi - x_min) * canvas_width / (x_max - x_min)
        y_pixel = canvas_height - (yi - y_min) * canvas_height / (y_max - y_min)
        canvas.create_oval(x_pixel, y_pixel, x_pixel + 2, y_pixel + 2, fill="blue")

    # Отображение координатных плоскостей и значений
    for i in range(11):
        x_value = x_min + i * x_interval
        x_pixel = i * canvas_width / 10
        canvas.create_line(x_pixel, 0, x_pixel, canvas_height, fill="gray")
        canvas.create_text(x_pixel, canvas_height + 10, text=f"{x_value:.2f}", anchor="n")

        y_value = y_min + i * y_interval
        y_pixel = canvas_height - i * canvas_height / 10
        canvas.create_line(0, y_pixel, canvas_width, y_pixel, fill="gray")
        canvas.create_text(canvas_width + 10, y_pixel, text=f"{y_value:.2f}", anchor="w")

    # Отображение точек, по которым построен график
    for xi, yi in zip(x_values, y_values):
        x_pixel = (xi - x_min) * canvas_width / (x_max - x_min)
        y_pixel = canvas_height - (yi - y_min) * canvas_height / (y_max - y_min)
        canvas.create_oval(x_pixel - 3, y_pixel - 3, x_pixel + 3, y_pixel + 3, fill="red")


# Функция для изменения масштаба
def zoom_in():
    global canvas_width, canvas_height
    canvas_width *= 1.2
    canvas_height *= 1.2
    canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
    plot_interpolation()


def zoom_out():
    global canvas_width, canvas_height
    canvas_width /= 1.2
    canvas_height /= 1.2
    canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
    plot_interpolation()


# Функция для перемещения камеры
def move(direction):
    dx, dy = 0, 0
    if direction == "up":
        dy = -20
    elif direction == "down":
        dy = 20
    elif direction == "left":
        dx = -20
    elif direction == "right":
        dx = 20
    canvas.scan_dragto(dx, dy, gain=1)
    plot_interpolation()


# Создание основного окна
root = tk.Tk()
root.title("Интерполяция по Лагранжу")

# Создание и размещение элементов интерфейса
frame = tk.Frame(root)
frame.pack()

x_entries = []
y_entries = []

for i in range(5):
    x_label = tk.Label(frame, text="x" + str(i) + ":")
    x_label.grid(row=i, column=0)
    x_entry = tk.Entry(frame)
    x_entry.grid(row=i, column=1)
    x_entries.append(x_entry)

    y_label = tk.Label(frame, text="y" + str(i) + ":")
    y_label.grid(row=i, column=2)
    y_entry = tk.Entry(frame)
    y_entry.grid(row=i, column=3)
    y_entries.append(y_entry)

plot_button = tk.Button(frame, text="Построить интерполяцию", command=plot_interpolation)
plot_button.grid(row=5, columnspan=4)

zoom_in_button = tk.Button(root, text="Увеличить", command=zoom_in)
zoom_in_button.pack(side="left")
zoom_out_button = tk.Button(root, text="Уменьшить", command=zoom_out)
zoom_out_button.pack(side="left")

move_up_button = tk.Button(root, text="Вверх", command=lambda: move("up"))
move_up_button.pack(side="left")
move_down_button = tk.Button(root, text="Вниз", command=lambda: move("down"))
move_down_button.pack(side="left")
move_left_button = tk.Button(root, text="Влево", command=lambda: move("left"))
move_left_button.pack(side="left")
move_right_button = tk.Button(root, text="Вправо", command=lambda: move("right"))
move_right_button.pack(side="left")

# Создание и настройка холста для отображения графика
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

root.mainloop()