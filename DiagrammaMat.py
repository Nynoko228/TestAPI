import matplotlib.pyplot as plt
import numpy as np

# Задайте задачи и время начала их выполнения
tasks = ["Задача 1", "Задача 2", "Задача 3"]
start_dates = ["2023-10-26", "2023-10-27", "2023-10-28"]
end_dates = ["2023-10-30", "2023-10-29", "2023-10-31"]


# Преобразуйте даты в числовой формат
start_dates = [np.datetime64(date) for date in start_dates]
end_dates = [np.datetime64(date) for date in end_dates]

# Создайте фигуру и оси
fig, ax = plt.subplots(figsize=(10, 6))

# Отобразите задачи как горизонтальные полосы
for i, task in enumerate(tasks):
    ax.barh(task, end_dates[i] - start_dates[i], left=start_dates[i], color='b', alpha=0.7, label=task)

# Настройте оси и заголовок
ax.set_xlabel('Время')
ax.set_title('Диаграмма Ганта')
ax.legend(loc='upper right')

# Отобразите диаграмму
plt.show()