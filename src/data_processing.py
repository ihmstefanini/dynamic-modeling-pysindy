"""Data proccessing step """
from typing import Tuple
import numpy as np
import pandas as pd

from src.common import ORIGINAL_DATA_DIR, PROCESSED_DATA_DIR
from src.utils import standardise


def load_data() -> pd.DataFrame:
    """
        # Summary

            Reads data set from csv file.

        Args:
            None

        Returns:
            (pd.DataFrame): a pandas dataframe with columns: Timestamp, FIC1.PV, FIC1.CV, FIC1.SP,
            FIC2.PV, FIC2.CV, FIC2.SP
    """

    data = pd.read_csv(f"{ORIGINAL_DATA_DIR}/data.csv", index_col=0)

    data.index = pd.to_datetime(data.index)
    data.dropna(inplace=True)

    return data


def get_processed_data(example_1: bool, sample_size: int) -> pd.DataFrame:
    """
        # Summary

            Process data in order to have a sample of the dataset.

        Args:
            example_1 (bool): if True, returns the first flow control loop data of the dataset.
            example_1 (bool): if False, returns the second flow control loop data of the dataset.
            sample_size (int): the size of the sample.

        Returns:
            (pd.DataFrame): a pandas dataframe with columns: Timestamp, FICx.PV, FICx.CV, FICx.SP
    """

    data = load_data()

    if example_1:
        # Simplyfing columns names
        data.rename({'FIC1.PV': 'PV', 'FIC1.CV': 'CV',
                    'FIC1.SP': 'SP'}, axis=1, inplace=True)
        data.drop(['FIC2.PV', 'FIC2.CV', 'FIC2.SP'], axis=1, inplace=True)

    else:
        data.rename({'FIC2.PV': 'PV', 'FIC2.CV': 'CV',
                     'FIC2.SP': 'SP'}, axis=1, inplace=True)
        data.drop(['FIC1.PV', 'FIC1.CV', 'FIC1.SP'], axis=1, inplace=True)

    date_start = pd.to_datetime('2020-07-04 00:00:00')
    date_end = pd.to_datetime('2020-07-05 00:00:00')
    processed_data = data.loc[date_start:date_end]

    if sample_size is not None:
        processed_data = processed_data[:sample_size]

    return processed_data


def get_train_test_data(processed_data: pd.DataFrame, split_percent: float,
                        sample_size: int, t0:float, dt: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
        # Summary

            Process data in order to have a sample of the dataset.

        Args:
            example_1 (bool): if True, returns the first flow control loop data of the dataset.
            example_1 (bool): if False, returns the second flow control loop data of the dataset.
            sample_size (int): the size of the sample.

        Returns:
            (pd.DataFrame): a pandas dataframe with columns: Timestamp, FICx.PV, FICx.CV, FICx.SP
    """
    u_train, u_test = standardise(processed_data.CV[:int(
        sample_size * split_percent)]).to_numpy(), standardise(processed_data.CV[int(sample_size * split_percent):]).to_numpy()
    x_train, x_test = standardise(processed_data.PV[:int(
        sample_size * split_percent)]).to_numpy(), standardise(processed_data.PV[int(sample_size * split_percent):]).to_numpy()

    tmax = x_train.shape[0]
    n = int(tmax / dt)
    t_train = np.linspace(start=t0, stop=tmax, num=n)

    return x_train, x_test, u_train, u_test, t_train

    return processed_data
