import pandas as pd
from tabulate import tabulate

def read_data(path="~/data/parquet"):
    df = pd.read_parquet(path)

    return df

def top(dt,top):
    df = read_data()
    fdf=df[df['dt']==dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(top)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()

    return cnt

def pretty(dt,top):
    df = read_data()
    fdf=df[df['dt']==dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(top)
    ddf = sdf.drop(columns=['dt'])
    pdf = tabulate(ddf,headers=["No.","useCmd","useCnt"],tablefmt="outline")

   # r = pdf.to_string(index=False)
   # return r
    return pdf

