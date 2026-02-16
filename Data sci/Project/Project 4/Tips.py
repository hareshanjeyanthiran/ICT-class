import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"F:\Hareshan\ICT class\Data sci\Project\Project 4\Tips Dataset.csv")

print(df.head())

print(df[['size', 'tip', 'total_bill']].describe())
df[['size', 'tip', 'total_bill']].hist(bins=20, figsize=(8,6))
plt.show()

plt.figure()
sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Count")
plt.show()


plt.figure()
sns.scatterplot(data=df,x='total_bill',y='tip',hue='time')
plt.title("Total Bill vs Tip (Colored by Time)")
plt.show()


sns.pairplot(df,hue='gender')
plt.show()