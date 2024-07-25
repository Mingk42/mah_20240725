from mingk42_args_history.db.utils import read_data
import pandas as pd

def test_hello():
    df=read_data()
    assert isinstance(df, pd.DataFrame)
