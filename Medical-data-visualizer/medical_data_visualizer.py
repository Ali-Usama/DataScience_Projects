import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height']/ 100) ** 2)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['overweight'] = df['overweight'].apply(lambda x: 1 if x>25 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x==1 else 1)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_melt = df.melt(id_vars='cardio',
                 value_vars=['active', 'alco', 'cholesterol', 'gluc','overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_melt.groupby(['cardio', 'variable', 
                                       'value'])['value'].count()).rename(columns={
    									'value': 'total'}).reset_index()

    # Draw the catplot with 'sns.catplot()'
    draw = sns.catplot(x = 'variable', 
                   y = 'total', kind = 'bar',
                 data = df_cat, hue='value',
                 col='cardio')
                 
    fig = draw.fig

    # Save figure:
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
             (df['height'] >= df['height'].quantile(0.025)) &
              (df['height'] <= df['height'].quantile(0.975)) &
             (df['weight'] >= df['weight'].quantile(0.025)) &
             (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (9,9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, linewidths=.5, mask=mask,
           vmax=.25, center=0,
            annot=True, fmt = '.1f',
            square = True, vmin=-0.1,
           cbar_kws={'shrink' : .45,
                    'format' : '%.2f'})

    # Save figure:
    fig.savefig('heatmap.png')
    return fig
