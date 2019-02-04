import pandas as pd
import os
import sqlite3
import argparse
import json

#input_data = input("Write CSV file name....    ")
#f_path = open(os.path.join(input_data), "r") 
#print (os.path.realpath('datafile.csv') )
parser = argparse.ArgumentParser()
parser.add_argument('filename', help="File Name")
arg = parser.parse_args()
f_path = open(os.path.join(arg.filename), "r")   
df = pd.read_csv(f_path)
print(df)

conn = sqlite3.connect('csvdata.db')

conn.execute('''CREATE TABLE IF NOT EXISTS PERSON(
         ID INT PRIMARY KEY ,
         TIME           TIMESTAMP,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')


df.to_sql('PERSON',conn, if_exists='append', index=False)
inserted_data = len(df)
print("Total Data Inserted in Database  :", inserted_data)
total_data = conn.execute("select count(*) from person") 
for value in total_data:
    print("Total Records :",value) 
