import numpy as np
def iqr(column):
    """Inter-quartile range, which is the 75th percentile minus the 25th percentile"""
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))