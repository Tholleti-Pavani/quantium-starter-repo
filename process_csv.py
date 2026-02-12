import pandas as pd

# Read CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Normalize product names and keep only pink morsels
df1 = df1[df1['product'].str.strip().str.lower() == "pink morsel"]
df2 = df2[df2['product'].str.strip().str.lower() == "pink morsel"]
df3 = df3[df3['product'].str.strip().str.lower() == "pink morsel"]

# Remove $ sign from price and convert to float
df1['price'] = df1['price'].replace(r'[\$,]', '', regex=True).astype(float)
df2['price'] = df2['price'].replace(r'[\$,]', '', regex=True).astype(float)
df3['price'] = df3['price'].replace(r'[\$,]', '', regex=True).astype(float)


# Calculate Sales
df1['Sales'] = df1['quantity'] * df1['price']
df2['Sales'] = df2['quantity'] * df2['price']
df3['Sales'] = df3['quantity'] * df3['price']

# Keep only required columns
df1 = df1[['Sales', 'date', 'region']]
df2 = df2[['Sales', 'date', 'region']]
df3 = df3[['Sales', 'date', 'region']]

# Combine all CSVs
combined_df = pd.concat([df1, df2, df3])

# Save to a new CSV file
combined_df.to_csv("data/formatted_output.csv", index=False)

print("CSV files processed successfully!")

