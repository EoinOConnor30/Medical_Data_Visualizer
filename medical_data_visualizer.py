import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where(df['weight']/((df['height']/100)**2)>25, 1, 0)

# 3
df['cholesterol']=np.where(df['cholesterol']==1, 0, 1)
df['gluc']=np.where(df['gluc']==1, 0, 1)

# 4
def draw_cat_plot():

    # 5
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars=['cardio'])
    df_cat = df_cat.sort_values(by=['cardio'])
    df_cat = df_cat.groupby(df_cat.columns.tolist(), as_index=False).size()
    

    # 7


    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='size', col='cardio', hue='value', kind='bar')


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.drop(df[(df['ap_lo']>df['ap_hi']) | (df['height']<df['height'].quantile(0.025)) | (df['height']>df['height'].quantile(0.975)) | (df['weight']<df['weight'].quantile(0.025)) | (df['weight']>df['weight'].quantile(0.975))].index)
    # 12
    corr = df_heat.corr(method='pearson')
    
    # 13
    mask = np.triu(np.ones_like(corr))



    # 14
    fig, ax = plt.subplots(figsize=(10,8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig




