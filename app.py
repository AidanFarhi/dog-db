import sqlite3
import pandas as pd

urls = []
base_url = 'https://afarhidev-data-swamp.s3.amazonaws.com/ofa/ke/KE-'
for year in range(2006, 2025):
    urls.append(f'{base_url}{year}.csv')

dfs = []
for url in urls:
    df = pd.read_csv(url)
    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

conn = sqlite3.connect('dog.db')
cursor = conn.cursor()

final_df.to_sql('dog_health', conn, index=False, if_exists='replace')

cursor.execute('select * from dog_health limit 10')
for row in cursor.fetchall():
    print(row)

cursor.execute('PRAGMA table_info(dog_health)')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
