import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Actual Data')

    # Line of best fit using all data
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = range(df['Year'].min(), 2051)
    plt.plot(years_all, [slope*x + intercept for x in years_all], color='red', label='Fit 1880-2014')

    # Line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, [slope2*x + intercept2 for x in years_recent], color='green', label='Fit 2000-2014')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot
    plt.savefig("sea_level_plot.png")
    return plt.gcf()

# Run the function if executed directly
if __name__ == "__main__":
    draw_plot()
    print("Plot created and saved as sea_level_plot.png")