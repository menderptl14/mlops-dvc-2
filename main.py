import os
import pandas as pd

data = {
    'name' : ['mahir','angel'],
    'age' : [19,20],
    'city' : ['udpr','jp']
}

df = pd.DataFrame(data)

new_raw = {'name':'gf1','age':14,'city':'delhi'}
df.loc[len(df.index)] = new_raw

data_dir = 'data'

os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved at {file_path}")
