import numpy as np
import matplotlib.pyplot as plot

plot.rcParams['figure.figsize'] = [10, 7]

def plot_trig():
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    y1 = np.tanh(x)
    y2 = np.sin(x)
    fig, axes = plot.subplots(1, 2, sharey=True)
    axes[1].plot(x, y1)
    axes[1].plot(x, -y1)
    axes[0].plot(x, y2)
    plot.show()

if __name__ == '__main__':
    plot_trig()
