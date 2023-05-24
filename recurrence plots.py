import numpy as np
import matplotlib.pyplot as plt
from pyts.image import RecurrencePlot

def recurrence_plot(ts, time_points, delay = 1, eps = 0.05, filename = "rp"):
    """
    :param ts: a np.array time series
    :param time_points: observation times of time series
    :param delay: time gap between two back-to-back points of the time series
    :param eps: threshold for the maximum distance to be considered recurrent
    :param filename: name under which the recurrence plot is saved

    Shows and saves a recurrence plot.
    """

    rec_plot = RecurrencePlot(time_delay = delay,
                              threshold = eps)

    # transform time series into a recurrence plot
    ts_rp = rec_plot.transform(ts)

    # plot figure
    plt.figure(figsize=(5,5))
    plt.imshow(ts_rp[0], cmap = "binary", origin = "lower")
    plt.title("Recurrence Plot", fontsize = 18)
    plt.tight_layout()

    # save figure
    filename = "Figures/" + filename
    plt.savefig(filename)

    # show figure
    plt.show()


if __name__ == "__main__":

    # Create a toy time series using the sine function
    time_points = np.linspace(0, 4 * np.pi, 1000)
    x = np.sin(time_points)
    X = np.array([x])

    # Create recurrence
    recurrence_plot(X, time_points, eps = np.pi/18, filename = "sin")