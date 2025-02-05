import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = np.where(df['weight'] / (df['height']/100)**2 > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby('cardio', as_index=False).value_counts().sort_values(by=['variable'])
    df_cat.columns = ['cardio', 'variable', 'value', 'total']
    

    # 7
    sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar', errorbar=None)


    # 8
    fig = plt.gcf()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr().round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig = plt.figure(figsize=(10,8))

    # 15
    sns.heatmap(corr, cmap='cubehelix', annot=True, fmt='0.1f', square=True, mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig
