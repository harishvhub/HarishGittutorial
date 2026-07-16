import pandas as pd

# Load your data
df = pd.read_csv('Customers.csv')

# Convert and save as JSON
df.to_json('data.json', orient='records', indent=4)

# Load JSON file into a DataFrame dataset
df = pd.read_json('data.json')

# View the first 5 rows
print(df.head())

df.to_csv('output.to_pandas.csv', index=False)

print("JSON successfully converted to CSV using Pandas!")

