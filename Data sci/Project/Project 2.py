import pandas as pd
import numpy as np

# 1️⃣ Create a dictionary with null values
data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [100, 200, None, None]
}

# 2️⃣ Create a DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# 3️⃣ Print first 2 and last 2 rows
print("First 2 rows:")
print(df.head(2))
print("\n")

print("Last 2 rows:")
print(df.tail(2))
print("\n")

# 4️⃣ Total number of null values
print("Total number of null values:")
print(df.isnull().sum().sum())
print("\n")

# 5️⃣ Detailed information of the DataFrame
print("DataFrame Info:")
df.info()
print("\n")

