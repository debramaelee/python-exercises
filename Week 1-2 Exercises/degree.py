import matplotlib.pyplot as plot

def f(x):
    return x * 1.8

x = int(raw_input("What is the temperature in Celcius? "))

xs = range(-100, 100)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
