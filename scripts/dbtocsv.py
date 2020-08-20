import pandas as pd
from simpledbf import Dbf5
from pathlib import Path

folder_name = input("What is the folder's name?")
dbfpath = Path('./scripts/dbfiles')
csv_path = f'./scripts/{folder_name}/'
dbf_names = [str(i) for i in dbfpath.iterdir() if '.gitignore' not in str(i)]
csv_names = [i.split('/')[-1].split('.')[0] for i in dbf_names]


for i, v in enumerate(dbf_names):
    dbf = Dbf5(v, codec='Latin-1')
    df = dbf.to_dataframe()
    df.to_csv(csv_path + csv_names[i] + '.csv')
