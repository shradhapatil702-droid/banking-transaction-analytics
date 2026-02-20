import pandas as pd
df=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\banking-transaction-analytics\data\raw_data\raw_banking_dataset.csv")
df.columns = df.columns.str.strip()

amount_cols=["WITHDRAWAL AMT","DEPOSIT AMT","BALANCE AMT"]

for col in amount_cols:
    df[col]=df[col].astype(str).str.replace(",","")
    df[col]=pd.to_numeric(df[col],errors="coerce")

#replace missing values
df["WITHDRAWAL AMT"]=df["WITHDRAWAL AMT"].fillna(0)
df["DEPOSIT AMT"]=df["DEPOSIT AMT"].fillna(0)

df["Account No"]=df["Account No"].str.replace("'","")

df["DATE"]=pd.to_datetime(df["DATE"],errors="coerce")

df.to_csv(r"C:\Users\hp\OneDrive\Desktop\banking-transaction-analytics\data\processed_data\cleaned_bank_transactions.csv")

print("data cleaning completed successfully")
