import pandas as pd
import numpy as np


data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [100, 200, None, None]
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")


print("First 2 rows:")
print(df.head(2))
print("\n")

print("Last 2 rows:")
print(df.tail(2))
print("\n")


print("Total number of null values:")
print(df.isnull().sum().sum())
print("\n")


print("DataFrame Info:")
df.info()
print("\n")

