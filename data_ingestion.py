import pandas as pd
import numpy as np
import os

def load_data(path):
    df = pd.read_csv(path)
    return df
