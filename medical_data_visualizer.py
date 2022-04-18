import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df =  pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'])/((df['height'] * (10**-2))** 2).round(2)

df['overweight'] = np.where(df['overweight'] > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1,0,1)

df['gluc'] = np.where(df['gluc'] == 1, 0, 1) 
  

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars= 
    ['active', 'alco', 'cholesterol','gluc', 
    'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =  pd.melt(df, id_vars=['cardio'], value_vars= 
    ['active', 'alco', 'cholesterol','gluc', 
    'overweight', 'smoke'])
  
    # Draw the catplot with 'sns.catplot()'
    fig= sns.catplot(data=df_cat, kind='count',     
                    x='variable', hue='value', 
                 col='cardio')
    fig.set(xlabel="variable", ylabel = "total")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
  
    df.drop(df[df['ap_lo'] > df['ap_hi']].index, inplace=True)  
  
    df.drop(df[df['height'] < df['height'].quantile(0.025)].index, inplace=True)
  
    df.drop(df[df['height'] > df['height'].quantile(0.975)].index, inplace=True) 
  
    df.drop(df[df['weight'] < df['weight'].quantile(0.025)].index, inplace=True)  
  
    df.drop(df[df['weight'] > df['weight'].quantile(0.975)].index, inplace=True)
  
    df_heat= df
    
    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig = plt.figure(figsize=(9, 8))

    # Draw the heatmap with 'sns.heatmap()'
    fig= sns.heatmap(corr, mask= mask, center=0,
                     vmin= -0.08, vmax= 0.24, 
                     annot= True,  fmt= "0", 
                     square=True,         
                     linewidths=.5,
                     cbar_kws= {"shrink": .5})

    fig = fig.get_figure() 
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


