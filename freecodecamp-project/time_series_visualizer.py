# Step 0: Imports at the top
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load & clean the data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]

# Step 2: Line Plot Function
def draw_line_plot():
    data = df.copy()  # copy to avoid modifying original
    plt.figure(figsize=(15,5))
    plt.plot(data.index, data['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.savefig("line_plot.png")
    return plt.gcf()

# Step 3: Bar Plot Function
def draw_bar_plot():
    data = df.copy()
    data['year'] = data.index.year
    data['month'] = data.index.month_name()
    monthly_avg = data.groupby(['year', 'month'])['value'].mean().unstack()
    month_order = ['January','February','March','April','May','June','July',
                   'August','September','October','November','December']
    monthly_avg = monthly_avg[month_order]
    monthly_avg.plot(kind='bar', figsize=(15,7))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.savefig("bar_plot.png")
    return plt.gcf()

# Step 4: Box Plot Function
def draw_box_plot():
    data = df.copy().reset_index()
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')
    data['month_num'] = data['date'].dt.month
    data = data.sort_values('month_num')
    
    fig, axes = plt.subplots(1, 2, figsize=(20,6))
    
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    plt.savefig("box_plot.png")
    return fig