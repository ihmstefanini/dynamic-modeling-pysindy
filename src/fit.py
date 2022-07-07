"""Fits the model using PySindy."""

import argparse
from ast import IsNot
import logging
import pickle
from pathlib import Path
from typing import Tuple

import h5py
import numpy as np
import pandas as pd
import pysindy as ps

from pysindy.differentiation import FiniteDifference, SINDyDerivative, SmoothedFiniteDifference
from pysindy.optimizers import STLSQ

from src.common import (
    PROCESSED_DATA_DIR, MAX_ITERATIONS, OUTPUT_DIR, THRESHOLD)
from src.utils import standardise


def fit_u_x(u_train: np.ndarray,
            x_train: np.ndarray, t_train: np.ndarray, dt: float) -> Tuple[ps.SINDy]:
    """Uses PySINDy to find the equation that best fits the data u.
    """
    optimizer = STLSQ(threshold=THRESHOLD, max_iter=MAX_ITERATIONS)

    # Get a model for u and x
    logging.info("Model fitting for u and y without differentiation")
    x = x_train

    model_uy = ps.SINDy(optimizer=optimizer,
                        feature_names=["x", "u"],
                        discrete_time=True)
    model_uy.fit(x, u=u_train, t=dt, ensemble=True)
    logging.info("coefficients: %s", model_uy.coefficients().T)

    return (model_uy)


def fit_u_x_xdot(u_train: np.ndarray,
                 x_train: np.ndarray, t_train: np.ndarray, smoothed_diff: bool, dt: float) -> Tuple[ps.SINDy, np.ndarray]:
    """Uses PySINDy to find the equation that best fits the data u.
    """

    optimizer = STLSQ(threshold=THRESHOLD, max_iter=MAX_ITERATIONS)

    if smoothed_diff is False:
        differentiation_method = FiniteDifference()
        x_train_dot = differentiation_method._differentiate(x_train, t_train)
    else:
        differentiation_method = SmoothedFiniteDifference()
        x_train_dot = differentiation_method._differentiate(x_train, t_train)

    # Get a model for u and y and ydot
    logging.info("Model fitting for u and y with differentiation")
    x = x_train
    xdot = x_train_dot
    data_x_train = np.stack((x, xdot), axis=-1)
    model_uy_ydot = ps.SINDy(optimizer=optimizer,
                             differentiation_method=differentiation_method,
                             feature_names=["x", "xdot", "u"],
                             discrete_time=True)
    model_uy_ydot.fit(data_x_train, u=u_train, t=dt, ensemble=True)
    logging.info("coefficients: %s", model_uy_ydot.coefficients().T)

    return (model_uy_ydot, xdot)
