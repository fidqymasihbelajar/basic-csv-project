import pandas as pd
from datetime import datetime

name_input = str(input("Enter your full name: "))
idnumber_input = int(input("Enter your badge number: "))
job_function_input = str(input("Enter your Job Function: "))

record = {
    'Name': name_input,
    'Badge Number': idnumber_input,
    'Job Function': job_function_input,
    'Timestamp': datetime.now()
}

record_df = pd.DataFrame([record])

csv_path = 'database_of_mainpy.csv'
try:
    df = pd.read_csv(csv_path, sep=';')
    df = pd.concat([df,record_df], ignore_index=True)
except FileNotFoundError:
    df = record_df

df.to_csv(csv_path, sep=';', index=False)