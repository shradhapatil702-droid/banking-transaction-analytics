import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

df=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\banking-transaction-analytics\data\processed_data\cleaned_bank_transactions.csv")

username="root"
password= quote_plus("Shradha@2727")
host = "127.0.0.1"
database = "banking_analytics"

engine=create_engine(
    f"mysql+pymysql://{username}:{password}@127.0.0.1:3306/{database}"
)

df.to_sql("transactions", engine, if_exists="replace", index=False)

print("Connection Successful")
