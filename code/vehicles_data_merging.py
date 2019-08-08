import os
import glob
import pandas as pd

path = "../data/raw"
files = glob.glob(os.path.join(path, "pojazdy*.csv"))
df = pd.concat(pd.read_csv(file, low_memory=False) for file in files)
df.to_csv("../data/raw/Vehicles.csv")
