#  Monthly Sales Visualization

import matplotlib.pyplot as plt

# Data:

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [ 12000, 15000, 13500, 18000, 21000, 19500,
    23000, 25000, 22000, 28000, 30000, 35000 ]

# Line Chart

plt.figure(figsize=(10,5))
plt.plot(months,sales,marker='o',linewidth=2,label="Monthly Sales")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales(pkr)")

plt.grid(True)
plt.legend()

plt.savefig( "Monthly_Sales_line.png",dpi=300,bbox_inches="tight")
plt.show()

# Bar Chart

plt.figure(figsize=(10,5))
plt.bar(months,sales)

plt.title("Monhtlu Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (pkr)")

plt.grid(axis="y",alpha=0.3)

plt.tight_layout()

plt.savefig( "monthly_sales_bar.png",dpi=300,bbox_inches="tight")

plt.show()

# Scatter Plot

month_numbers = list(range(1,13))
plt.figure(figsize=(10, 5))

plt.scatter(month_numbers,sales,s=80)

plt.title("Monthly Sales Distribution")
plt.xlabel("Month Number")
plt.ylabel("Sales (PKR)")

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig("monthly_sales_scatter.png",dpi=300,bbox_inches="tight")

plt.show()

