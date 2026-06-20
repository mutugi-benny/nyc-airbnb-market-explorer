import pandas as pd

# Load and check
df = pd.read_csv('data/raw/listings.csv')
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(df.head())