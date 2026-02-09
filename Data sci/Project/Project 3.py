import pandas as pd
import matplotlib.pyplot as plt


month_number = [1,2,3,4,5,6,7,8,9,10,11,12]
facecream   = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash    = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpaste  = [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingsoap = [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo     = [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
total_units  = [21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020]
total_profit = [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]

df = pd.DataFrame({
    "Month": month_number,
    "Face Cream": facecream,
    "Face Wash": facewash,
    "Toothpaste": toothpaste,
    "Bathing Soap": bathingsoap,
    "Shampoo": shampoo,
    "Moisturizer": moisturizer,
    "Total Units": total_units,
    "Total Profit": total_profit
})

plt.plot(df["Month"], df["Total Profit"], linestyle=':', marker='o',linewidth=3, color='red', markerfacecolor='black')
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Company Profit Per Month")
plt.show()

plt.plot(df["Month"], df["Face Cream"], marker='o', linewidth=3, label="Face Cream")
plt.plot(df["Month"], df["Face Wash"], marker='o', linewidth=3, label="Face Wash")
plt.plot(df["Month"], df["Toothpaste"], marker='o', linewidth=3, label="Toothpaste")
plt.plot(df["Month"], df["Bathing Soap"], marker='o', linewidth=3, label="Bathing Soap")
plt.plot(df["Month"], df["Shampoo"], marker='o', linewidth=3, label="Shampoo")
plt.plot(df["Month"], df["Moisturizer"], marker='o', linewidth=3, label="Moisturizer")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.title("Monthly Sales Data of All Products")
plt.legend()
plt.show()

plt.bar(df["Month"], df["Face Cream"], width=0.4, label="Face Cream")
plt.bar([m + 0.4 for m in df["Month"]], df["Face Wash"], width=0.4, label="Face Wash")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.title("Face Cream vs Face Wash Sales Per Month")
plt.legend()
plt.show()