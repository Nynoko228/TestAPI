import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления интерполяционного полинома Лагранжа
def lagrange_interpolation(x, y, x_interpolate):
    result = 0
    n = len(x)
    for j in range(n):
        term = y[j]
        for i in range(n):
            if i != j:
                term *= (x_interpolate - x[i]) / (x[j] - x[i])
        result += term
    return result

# Исходные данные для интерполяции
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 0.5, 0.2, 0.1, 0.05])

# Генерация точек для отображения графика
x_interpolate = np.linspace(1, 5, 100)
y_interpolate = [lagrange_interpolation(x, y, xi) for xi in x_interpolate]

# Создание графика
plt.figure(figsize=(8, 6))
plt.plot(x_interpolate, y_interpolate, label='Интерполяция Лагранжа')
plt.scatter(x, y, color='red', label='Исходные точки')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Интерполяция по Лагранжу')
plt.grid(True)

plt.show()
