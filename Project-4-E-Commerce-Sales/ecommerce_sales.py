import matplotlib.pyplot as plt

# ==================================================
# DATA
# ==================================================

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [
    45000, 52000, 48000, 60000, 65000, 72000,
    68000, 75000, 82000, 90000, 105000, 120000
]

profit = [
    9000, 11000, 8500, 13000, 15000, 17000,
    15500, 18000, 21000, 24000, 28000, 33000
]

orders = [
    120, 135, 128, 150, 165, 180,
    172, 190, 210, 235, 260, 300
]


products = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Keyboard",
    "Mouse"
]

product_sales = [
    350000,
    280000,
    150000,
    95000,
    70000
]


# ==================================================
# 1. MONTHLY SALES TREND
# ==================================================

fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(
    months,
    sales,
    marker="o",
    linewidth=2
)

ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (PKR)")

ax.grid(True, alpha=0.3)

# Highest sales point
max_sales = max(sales)
max_index = sales.index(max_sales)

ax.annotate(
    f"Highest: {max_sales:,}",
    xy=(months[max_index], max_sales),
    xytext=(months[max_index - 2], max_sales + 15000),
    arrowprops=dict(arrowstyle="->")
)

fig.tight_layout()

fig.savefig(
    "monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 2. PRODUCT SALES
# ==================================================

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    products,
    product_sales
)

ax.set_title("Sales by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Sales (PKR)")

# Add values to bars
for i, value in enumerate(product_sales):

    ax.text(
        value,
        i,
        f" {value:,}",
        va="center"
    )

ax.grid(
    axis="x",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "product_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 3. MONTHLY PROFIT
# ==================================================

fig, ax = plt.subplots(figsize=(11, 5))

ax.bar(
    months,
    profit
)

ax.set_title("Monthly Profit")
ax.set_xlabel("Month")
ax.set_ylabel("Profit (PKR)")

ax.grid(
    axis="y",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "monthly_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 4. ORDERS DISTRIBUTION
# ==================================================

fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(
    orders,
    bins=6,
    edgecolor="black"
)

ax.set_title("Order Volume Distribution")
ax.set_xlabel("Number of Orders")
ax.set_ylabel("Frequency")

ax.grid(
    axis="y",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "orders_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 5. SALES VS PROFIT
# ==================================================

fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    sales,
    profit,
    s=100
)

ax.set_title("Sales vs Profit")
ax.set_xlabel("Sales (PKR)")
ax.set_ylabel("Profit (PKR)")

ax.grid(True, alpha=0.3)

fig.tight_layout()

fig.savefig(
    "sales_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 6. PRODUCT CONTRIBUTION
# ==================================================

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    product_sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Product Contribution to Total Sales")

fig.tight_layout()

fig.savefig(
    "product_contribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 7. COMPLETE E-COMMERCE DASHBOARD
# ==================================================

fig, ax = plt.subplots(
    2,
    3,
    figsize=(16, 9)
)


# --------------------------------------------------
# Plot 1 — Sales Trend
# --------------------------------------------------

ax[0, 0].plot(
    months,
    sales,
    marker="o"
)

ax[0, 0].set_title("Sales Trend")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")

ax[0, 0].grid(
    True,
    alpha=0.3
)


# --------------------------------------------------
# Plot 2 — Product Sales
# --------------------------------------------------

ax[0, 1].barh(
    products,
    product_sales
)

ax[0, 1].set_title("Sales by Product")
ax[0, 1].set_xlabel("Sales")


# --------------------------------------------------
# Plot 3 — Monthly Profit
# --------------------------------------------------

ax[0, 2].bar(
    months,
    profit
)

ax[0, 2].set_title("Monthly Profit")
ax[0, 2].set_xlabel("Month")
ax[0, 2].set_ylabel("Profit")


# --------------------------------------------------
# Plot 4 — Orders
# --------------------------------------------------

ax[1, 0].plot(
    months,
    orders,
    marker="o"
)

ax[1, 0].set_title("Monthly Orders")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Orders")

ax[1, 0].grid(
    True,
    alpha=0.3
)


# --------------------------------------------------
# Plot 5 — Sales vs Profit
# --------------------------------------------------

ax[1, 1].scatter(
    sales,
    profit,
    s=80
)

ax[1, 1].set_title("Sales vs Profit")
ax[1, 1].set_xlabel("Sales")
ax[1, 1].set_ylabel("Profit")

ax[1, 1].grid(
    True,
    alpha=0.3
)


# --------------------------------------------------
# Plot 6 — Product Contribution
# --------------------------------------------------

ax[1, 2].pie(
    product_sales,
    labels=products,
    autopct="%1.1f%%"
)

ax[1, 2].set_title("Product Contribution")


# --------------------------------------------------
# Dashboard Title
# --------------------------------------------------

fig.suptitle(
    "E-Commerce Sales Dashboard",
    fontsize=20
)


# --------------------------------------------------
# Layout
# --------------------------------------------------

plt.tight_layout()

fig.savefig(
    "ecommerce_sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
