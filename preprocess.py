import pandas as pd
import numpy as np
import os
from datetime import datetime

df = pd.read_csv('HomeC.csv')
# df["time"] = pd.to_datetime(df["time"])

df2 = df[:-250000]
print(df2)
df2["time"] = pd.to_datetime(df2["time"],unit='s')


print(df2["time"])

df2.to_csv('HomeC2_cleaned.csv', index=False)