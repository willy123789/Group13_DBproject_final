import pandas as pd
import numpy as np
import os
from datetime import datetime

df = pd.read_csv('HomeC2_cleaned.csv')

df2 = df[["time","use [kW]","gen [kW]","House overall [kW]","Dishwasher [kW]","Furnace 1 [kW]","Furnace 2 [kW]","Home office [kW]"]]
df2.to_csv('HomeC_elec_cleaned.csv', index=False)
print(df2)