import matplotlib.pyplot as plt


# -----------------------------
# Data
# -----------------------------

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]


lahore_temp = [
    13, 16, 21, 27, 32, 35,
    34, 33, 31, 26, 20, 15
]

islamabad_temp = [
    10, 13, 18, 24, 29, 33,
    32, 31, 29, 24, 17, 12
]

karachi_temp = [
    19, 21, 25, 29, 31, 32,
    31, 30, 30, 29, 25, 21
]

peshawar_temp = [
    12, 15, 20, 26, 32, 36,
    35, 34, 31, 25, 19, 14
]

quetta_temp = [
    4, 7, 12, 18, 24, 29,
    28, 26, 22, 16, 10, 5
]


rainfall = [
    15, 20, 30, 35, 25, 10,
    80, 70, 40, 20, 10, 15
]


# ==================================================
# 1. Temperature Comparison — Multiple Line Chart
# ==================================================

plt.figure(figsize=(12, 6))

plt.plot(
    months,
    lahore_temp,
    marker="o",
    label="Lahore"
)

plt.plot(
    months,
    islamabad_temp,
    marker="o",
    label="Islamabad"
)

plt.plot(
    months,
    karachi_temp,
    marker="o",
    label="Karachi"
)

plt.plot(
    months,
    peshawar_temp,
    marker="o",
    label="Peshawar"
)

plt.plot(
    months,
    quetta_temp,
    marker="o",
    label="Quetta"
)

plt.title("Monthly Temperature Comparison")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "temperature_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 2. Rainfall — Bar Chart
# ==================================================

plt.figure(figsize=(12, 6))

plt.bar(
    months,
    rainfall
)

plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    "monthly_rainfall.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 3. Temperature vs Rainfall — Scatter
# ==================================================

# Lahore temperature used for comparison

plt.figure(figsize=(10, 6))

plt.scatter(
    lahore_temp,
    rainfall,
    s=100
)

plt.title("Lahore Temperature vs Rainfall")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "temperature_vs_rainfall.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 4. Complete Weather Dashboard
# ==================================================

fig, ax = plt.subplots(
    2,
    2,
    figsize=(14, 9)
)


# -----------------------------
# Top Left — Temperature
# -----------------------------

ax[0, 0].plot(
    months,
    lahore_temp,
    marker="o",
    label="Lahore"
)

ax[0, 0].plot(
    months,
    islamabad_temp,
    marker="o",
    label="Islamabad"
)

ax[0, 0].plot(
    months,
    karachi_temp,
    marker="o",
    label="Karachi"
)

ax[0, 0].plot(
    months,
    peshawar_temp,
    marker="o",
    label="Peshawar"
)

ax[0, 0].plot(
    months,
    quetta_temp,
    marker="o",
    label="Quetta"
)

ax[0, 0].set_title("Temperature Comparison")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Temperature (°C)")

ax[0, 0].legend()
ax[0, 0].grid(True, alpha=0.3)


# -----------------------------
# Top Right — Rainfall
# -----------------------------

ax[0, 1].bar(
    months,
    rainfall
)

ax[0, 1].set_title("Monthly Rainfall")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Rainfall (mm)")

ax[0, 1].grid(
    axis="y",
    alpha=0.3
)


# -----------------------------
# Bottom Left — Lahore
# -----------------------------

ax[1, 0].plot(
    months,
    lahore_temp,
    marker="o",
    linewidth=2
)

ax[1, 0].set_title("Lahore Temperature Trend")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Temperature (°C)")

ax[1, 0].grid(True, alpha=0.3)


# -----------------------------
# Bottom Right — Scatter
# -----------------------------

ax[1, 1].scatter(
    lahore_temp,
    rainfall,
    s=80
)

ax[1, 1].set_title("Temperature vs Rainfall")
ax[1, 1].set_xlabel("Temperature (°C)")
ax[1, 1].set_ylabel("Rainfall (mm)")

ax[1, 1].grid(True, alpha=0.3)


# -----------------------------
# Overall Title
# -----------------------------

fig.suptitle(
    "Pakistan Weather Visualization",
    fontsize=18
)


# -----------------------------
# Layout & Save
# -----------------------------

plt.tight_layout()

plt.savefig(
    "pakistan_weather_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
