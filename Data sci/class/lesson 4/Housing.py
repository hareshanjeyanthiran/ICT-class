import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'F:\Hareshan\ICT class\Data sci\lesson\lesson 4\USA_Housing.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)


sns.kdeplot(x=df['Price'])
plt.title("Price Distribution (KDE)")
plt.show()


sns.scatterplot(x='Avg. Area Income', y='Price', data=df)
plt.title("Income vs Price")
plt.show()


sns.jointplot(x='Avg. Area Income', y='Price', data=df)
plt.show()


sns.pairplot(df)
plt.show()


new_df = df.drop('Address', axis=1)

plt.figure(figsize=(8,6))
sns.heatmap(new_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()