import rioxarray
import os
import subprocess
import pandas as pd
import geopandas as gpd
from rasterio.enums import Resampling
import numpy as np
import matplotlib.pyplot as plt
import json
    

error_list = []
# Function to run a command
def run_command(command):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Command succeeded:", result.stdout)
    else:
        print("Command failed:", result.stderr)
        error_list.append(command)

trainlist = []
predictlist = []
modelfile = 'KindleBooksDataComix.csv'

comics = pd.read_csv(modelfile)
print(comics.columns)

runFlag = False
for index, row in comics.iterrows():
    
    
    asin = row['ISBN / ASIN (Amazon ID)']
    
    if 'Wolverine by Benjamin Percy Vol. 2 (Wolverine (2020-))' in row['Title']:
        runFlag = True
        
    if not runFlag:
        continue
        
    asin = asin[2:-1]
    print("running: ",index,row['Title'], asin)

    train = f"python unkindle.py " + asin
    run_command(train)
