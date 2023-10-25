import matplotlib.pyplot as plt

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"})
ax.axis("equal")

plt.show()