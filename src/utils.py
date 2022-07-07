import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def standardise(series):
    """Standardize a pandas series"""
    return (series - series.mean()) / series.std()


def train_plots(u_train, y_train):

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))

    axs[0].plot(y_train, linewidth=1)
    axs[0].set_title('Real data plots')
    axs[0].set_xlabel('Time stamps')
    axs[0].legend(['PV (x) real (train set)'], loc='best')

    axs[1].plot(u_train)
    axs[1].set_xlabel('Samples')
    axs[1].legend(['CV (u) real (ttrain set)'], loc='best')

    # adding horizontal grid lines
    for ax in axs:
        ax.yaxis.grid(False)
        ax.set_ylabel('Observed values')

    plt.show()


def simulate_plots(t_test: np.ndarray, X_test_sim: np.ndarray, y_test: np.ndarray, u_test: np.ndarray, xdot: np.ndarray):

    if xdot is None:
        fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))

        # plot scatters
        axs[0].plot(t_test, X_test_sim[:, 0], linewidth=1)
        axs[0].plot(t_test, y_test, linewidth=1)
        axs[0].set_title('Simulation of Model u and y without diff')
        axs[0].set_xlabel('Simulation steps')
        axs[0].legend(
            ['y simuated (PySindy)', 'y real (test set)'], loc='best')

        axs[1].plot(u_test)
        axs[1].set_xlabel('Simulation steps')
        axs[1].legend(['u real (test set)'], loc='best')

        # adding horizontal grid lines
        for ax in axs:
            ax.yaxis.grid(False)
            ax.set_ylabel('Observed values')
        plt.show()

    else:
        fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 6))

        # plot scatters
        axs[0].plot(t_test, X_test_sim[:, 0], linewidth=1)
        axs[0].plot(t_test, y_test, linewidth=1)
        axs[0].set_title('Simulation of Model u and y with diff')
        axs[0].set_xlabel('Simulation steps')
        axs[0].legend(
            ['y simuated (PySindy)', 'y real (test set)'], loc='best')

        axs[1].plot(u_test)
        axs[1].set_xlabel('Simulation steps')
        axs[1].legend(['u real (test set)'], loc='best')

        axs[2].plot(X_test_sim[:, 1])
        axs[2].set_xlabel('Simulation steps')
        axs[2].legend(['ydot (test set)'], loc='best')

        # adding horizontal grid lines
        for ax in axs:
            ax.yaxis.grid(False)
            ax.set_ylabel('Observed values')
        plt.show()
