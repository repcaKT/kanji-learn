from sqlalchemy import create_engine, types
import csv
import pandas as pd

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/kanji_learn")

df = pd.read_csv("backend/test_data/sentences_all_levels.csv",sep=';',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
df.to_sql('sentences',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name