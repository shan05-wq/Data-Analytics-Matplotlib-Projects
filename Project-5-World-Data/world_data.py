import matplotlib.pyplot as plt

# ==================================================
# DATA
# ==================================================

countries = [
    "Pakistan",
    "India",
    "China",
    "USA",
    "UK",
    "Germany",
    "Japan",
    "Canada",
    "Australia",
    "Brazil"
]


population = [
    250,
    1460,
    1410,
    350,
    69,
    84,
    123,
    40,
    27,
    212
]


gdp = [
    375,
    3900,
    18000,
    29000,
    3600,
    4700,
    4200,
    2200,
    1800,
    2200
]


life_expectancy = [
    67,
    68,
    78,
    77,
    81,
    81,
    84,
    83,
    83,
    76
]


internet_usage = [
    45,
    55,
    76,
    97,
    96,
    92,
    94,
    94,
    96,
    81
]


# ==================================================
# 1. POPULATION
# ==================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    countries,
    population
)

ax.set_title("Population by Country")
ax.set_xlabel("Country")
ax.set_ylabel("Population (Millions)")

ax.tick_params(
    axis="x",
    labelrotation=45
)

ax.grid(
    axis="y",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "population_by_country.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 2. GDP
# ==================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(
    countries,
    gdp
)

ax.set_title("GDP by Country")
ax.set_xlabel("GDP (Billion USD)")
ax.set_ylabel("Country")

ax.grid(
    axis="x",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "gdp_by_country.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 3. LIFE EXPECTANCY
# ==================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    countries,
    life_expectancy,
    marker="o",
    linewidth=2
)

ax.set_title("Life Expectancy by Country")
ax.set_xlabel("Country")
ax.set_ylabel("Life Expectancy (Years)")

ax.tick_params(
    axis="x",
    labelrotation=45
)

ax.grid(
    True,
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "life_expectancy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 4. INTERNET USAGE
# ==================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    countries,
    internet_usage
)

ax.set_title("Internet Usage by Country")
ax.set_xlabel("Country")
ax.set_ylabel("Internet Users (%)")

ax.tick_params(
    axis="x",
    labelrotation=45
)

ax.grid(
    axis="y",
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "internet_usage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 5. GDP VS LIFE EXPECTANCY
# ==================================================

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(
    gdp,
    life_expectancy,
    s=100
)

ax.set_title("GDP vs Life Expectancy")
ax.set_xlabel("GDP (Billion USD)")
ax.set_ylabel("Life Expectancy (Years)")

# Country labels
for i in range(len(countries)):

    ax.annotate(
        countries[i],
        (
            gdp[i],
            life_expectancy[i]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

ax.grid(
    True,
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "gdp_vs_life_expectancy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 6. GDP VS INTERNET USAGE
# ==================================================

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(
    gdp,
    internet_usage,
    s=100
)

ax.set_title("GDP vs Internet Usage")
ax.set_xlabel("GDP (Billion USD)")
ax.set_ylabel("Internet Usage (%)")

for i in range(len(countries)):

    ax.annotate(
        countries[i],
        (
            gdp[i],
            internet_usage[i]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

ax.grid(
    True,
    alpha=0.3
)

fig.tight_layout()

fig.savefig(
    "gdp_vs_internet_usage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 7. COMPLETE WORLD DATA DASHBOARD
# ==================================================

fig, ax = plt.subplots(
    2,
    3,
    figsize=(16, 10)
)


# --------------------------------------------------
# Population
# --------------------------------------------------

ax[0,0].bar(
    countries,
    population
)

ax[0, 0].set_title("Population")

ax[0,0].tick_params(
    axis="x",
    labelrotation=45
)


# --------------------------------------------------
# GDP
# --------------------------------------------------

ax[0, 1].barh(
    countries,
    gdp
)

ax[0, 1].set_title("GDP")


# --------------------------------------------------
# Life Expectancy
# --------------------------------------------------

ax[0, 2].plot(
    countries,
    life_expectancy,
    marker="o"
)

ax[0, 2].set_title("Life Expectancy")

ax[0, 2].tick_params(
    axis="x",
    labelrotation=45
)


# --------------------------------------------------
# Internet Usage
# --------------------------------------------------

ax[1, 0].bar(
    countries,
    internet_usage
)

ax[1, 0].set_title("Internet Usage")

ax[1, 0].tick_params(
    axis="x",
    labelrotation=45
)


# --------------------------------------------------
# GDP vs Life Expectancy
# --------------------------------------------------

ax[1, 1].scatter(
    gdp,
    life_expectancy,
    s=80
)

ax[1, 1].set_title(
    "GDP vs Life Expectancy"
)

ax[1, 1].set_xlabel("GDP")
ax[1, 1].set_ylabel("Life Expectancy")


# --------------------------------------------------
# GDP vs Internet
# --------------------------------------------------

ax[1, 2].scatter(
    gdp,
    internet_usage,
    s=80
)

ax[1, 2].set_title(
    "GDP vs Internet Usage"
)

ax[1, 2].set_xlabel("GDP")
ax[1, 2].set_ylabel("Internet Usage")


# --------------------------------------------------
# Overall Title
# --------------------------------------------------

fig.suptitle(
    "World Data Analysis Dashboard",
    fontsize=20
)


# --------------------------------------------------
# Layout
# --------------------------------------------------

plt.tight_layout()

fig.savefig(
    "world_data_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
