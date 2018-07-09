import matplotlib.pyplot as plt

x = [3, 2 , 1]
y = [1171.294, 589.754, 249.557]
z = [945.252, 421.998, 189.346]

my_xticks = ["100", "1k", "10k"]
plt.xticks(x, my_xticks)
plt.grid(axis='y')
plt.plot(x, y)
plt.plot(x, z)

plt.title("Execution time vs Dataset size [ranged query]")
plt.xlabel("Dataset size")
plt.ylabel("Time [ms]")



plt.show()

