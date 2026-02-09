import numpy as np
import pandas as pd
from pathlib import Path


def load_clean_data():
    """
    Load and minimally clean the event classification dataset.

    Returns
    -------
    X : pd.DataFrame
        Feature matrix (uncleaned, without scaling)
    y : np.ndarray
        Labels (0/1)
    w : np.ndarray
        Sample weights
    """

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "Data - Events" / "Particle-Physics-Event-Classification.csv"

    df = pd.read_csv(DATA_PATH)

    # Replace unphysical placeholders
    df = df.replace(-999, np.nan)

    y = df["Label"].map({"s": 1, "b": 0}).to_numpy()
    w = df["Weight"].to_numpy()

    X = df.drop(columns=["EventId", "Label", "Weight"])

    return X, y, w


from sklearn.model_selection import train_test_split

def split_data(
    X, y, w,
    random_state=42,
    holdout_size=0.3,   # (val + test)
    val_fraction=0.5    # fraction of holdout used for validation
):

    X_train, X_holdout, y_train, y_holdout, w_train, w_holdout = train_test_split(
        X, y, w,
        test_size=holdout_size,
        stratify=y,
        random_state=random_state
    )

    if val_fraction != 0:
        X_val, X_test, y_val, y_test, w_val, w_test = train_test_split(
            X_holdout, y_holdout, w_holdout,
            test_size=val_fraction,
            stratify=y_holdout,
            random_state=random_state
        )
    else:
        X_val, y_val, w_val = None, None, None
        X_test, y_test, w_test = X_holdout, y_holdout, w_holdout

    return (
        X_train, X_val, X_test,
        y_train, y_val, y_test,
        w_train, w_val, w_test
    )


from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def make_preprocessor():
    """
    Returns unfitted imputer and scaler.
    Fitting must be done on training data only.
    """
    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()
    return imputer, scaler

