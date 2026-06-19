import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the CSV file
df = pd.read_csv("medical_examination.csv")

# Add overweight column
df['overweight'] = (df['weight'] / (df['height']/100)**2).apply(lambda x: 1 if x > 25 else 0)

# Normalize data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    
    fig = sns.catplot(x="variable", hue="value", col="cardio",
                      data=df_cat, kind="count").fig

    # Save figure in current working directory
    save_path = os.path.join(os.getcwd(), "catplot.png")
    fig.savefig(save_path)
    return fig

def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12,10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, vmax=0.5, vmin=-0.1,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    save_path = os.path.join(os.getcwd(), "heatmap.png")
    fig.savefig(save_path)
    return fig