#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\user\Downloads\gamers.csv")

# 2. Display first 5 rows, shape, and data types
print ("===DATA SET SAMPLE===")
print(df.head()) 
print ("\n===DATA SHAPE===")
print(f"Dataset Shape: {df.shape}") 
print ("\n===DATA TYPES===")
print(df.dtypes)


# In[21]:


#Check for missing values
print("===== MISSING VALUES PER COLUMN =====")
print(df.isnull().sum())

print("\n===== COLUMNS WITH MISSING VALUES =====")
missing_cols = df.isnull().sum()
print(missing_cols[missing_cols > 0])



# In[31]:


#Data Cleaning
df = df.dropna(subset=['Year'])

print("\n===== COLUMNS WITH MISSING VALUES =====")
missing_cols = df.isnull().sum()
print(missing_cols[missing_cols > 0])

print ("\n====Convert the Year column to integers====")
df['Year'] = df['Year'].astype(int)

print ("===DATA SET SAMPLE====")
print (df.head())

print ("===DATA TYPE===")
print(df.dtypes)


# In[40]:


regional_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().sum()
print("====TOTAL REGIONAL SALES======")
print (regional_sales)

print("Total Global Sales:", df['Global_Sales'].sum())
print("Total Regional Sales:", df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum().sum())

print ("Difference:", df['Global_Sales'].sum() - df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum().sum())


# In[41]:


#summary statistics of sales columns
sales_cols = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']

print("=== SUMMARY STATISTICS OF SALES COLUMNS ===")
print(df[sales_cols].describe())


# In[52]:


#Top 10 games by Global_Sales.
print("=== TOP 10 GAMES BY GLOBAL SALES ===")

top10 = df.sort_values(by='Global_Sales', ascending=False).head(10)

print(top10[['Name','Platform','Year','Global_Sales']])
print("\n=== GENRE COUNT IN TOP 10 ===")
print(top10['Genre'].value_counts())

#Top 10 genres?
print("\n=== TOTAL COUNT OF EACH GENRE ===")
print(df['Genre'].value_counts())


# In[62]:


#Is success concentrated in some genres, and should the company focus on these genres? 
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

print("=== TOTAL GLOBAL SALES BY GENRE ===")
print(genre_sales)
avg_sales = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)

print("\n=== AVERAGE SALES PER GENRE ===")
print(avg_sales)

import matplotlib.pyplot as plt

genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

genre_sales.plot(kind='bar')

plt.title("Total Global Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Total Global Sales (Millions)")
plt.show()

avg_sales = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)

avg_sales.plot(kind='bar')

plt.title("Average Global Sales per Game by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Global Sales (Millions)")
plt.show()

genre_counts.plot(kind='bar')

plt.title("Number of Games per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.show()


# In[61]:


genre_total_sales.plot(kind='bar')

plt.title("Total Global Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Total Global Sales (Millions)")
plt.show()

genre_counts.plot(kind='bar')

plt.title("Number of Games per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.show()


# In[73]:


genre_summary = df.groupby('Genre').agg(
    Total_Sales=('Global_Sales','sum'),
    Game_Count=('Genre','count'))
print (genre_summary)

plt.figure()

plt.scatter(genre_summary['Game_Count'], genre_summary['Total_Sales'])

for genre in genre_summary.index:
    plt.text(
        genre_summary.loc[genre,'Game_Count'],
        genre_summary.loc[genre,'Total_Sales'],
        genre
    )

plt.title("Revenue vs Number of Games by Genre")
plt.xlabel("Number of Games Produced")
plt.ylabel("Total Global Sales (Millions)")
plt.show()


# In[77]:


import matplotlib.pyplot as plt

# 1. Setup the Canvas
plt.style.use('seaborn-v0_8-muted')
plt.figure(figsize=(12, 8))

# 2. Create the Scatter Plot
scatter = plt.scatter(
    genre_summary['Game_Count'], 
    genre_summary['Total_Sales'], 
    c=genre_summary['Total_Sales'], 
    cmap='viridis', 
    s=120, 
    alpha=0.8, 
    edgecolors='w'
)

# 3. Manual Labeling with a small "nudge"
for genre in genre_summary.index:
    plt.text(
        genre_summary.loc[genre, 'Game_Count'] + 8, # Moves text 8 units right
        genre_summary.loc[genre, 'Total_Sales'] + 8, # Moves text 8 units up
        genre,
        fontsize=10,
        fontweight='bold',
        va='bottom', # Vertical alignment
        ha='left'    # Horizontal alignment
    )

# 4. Final Aesthetics
plt.title("Video Game Genre Performance: Volume vs. Revenue", fontsize=16, pad=20)
plt.xlabel("Number of Games Produced", fontsize=12)
plt.ylabel("Total Global Sales (Millions USD)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Adding a colorbar to explain the 'c' mapping
plt.colorbar(scatter, label='Total Global Sales')

plt.tight_layout()
plt.show()


# In[78]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Aggregate sales by Genre
regional_stats = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()

# 2. Reshape the data for plotting (Long Format)
melted_df = regional_stats.melt(id_vars='Genre', var_name='Region', value_name='Sales')

# 3. Create the Visualization
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")

# Sort by NA_Sales for a cleaner visual flow
order = regional_stats.sort_values('NA_Sales', ascending=False)['Genre']

sns.barplot(data=melted_df, x='Genre', y='Sales', hue='Region', palette='viridis', order=order)

plt.title('Video Game Sales by Genre and Region', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Total Sales (Millions)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Region')

plt.tight_layout()
plt.show()


# In[79]:


import matplotlib.pyplot as plt
import seaborn as sns

# 1. Prepare the data
yearly_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()

# 2. Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_sales, x='Year', y='Global_Sales', marker='o', color='#2ca02c', linewidth=2.5)

# 3. Add Annotations for Context
plt.annotate('Wii/PS3 Era Peak', xy=(2008, 670), xytext=(2000, 750),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('COVID-19 Surge', xy=(2020, 500), xytext=(2012, 600),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('The Evolution of Gaming: Global Sales Over Time', fontsize=16)
plt.xlabel('Year of Release', fontsize=12)
plt.ylabel('Total Sales (Millions)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()


# In[81]:


import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 Data
top_games_data = {
    'Game': ['Tetris', 'Minecraft', 'GTA V', 'Wii Sports', 'RDR 2', 'Mario Kart 8', 'PUBG', 'Terraria', 'Witcher 3', 'Super Mario Bros'],
    'Sales': [520, 350, 225, 82.9, 82, 79, 75, 64, 60, 58]
}
df_top = pd.DataFrame(top_games_data)

# Visualizing
plt.figure(figsize=(12, 7))
sns.barplot(data=df_top, x='Sales', y='Game', hue='Game', palette='flare', legend=False)

plt.title('The All-Time Leaders: Global Sales (Millions)', fontsize=16, fontweight='bold')
plt.xlabel('Total Copies Sold (Millions)', fontsize=12)
plt.ylabel('Game Title', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Adding labels to bars
for i, val in enumerate(df_top['Sales']):
    plt.text(val + 5, i, f'{val}M', va='center', fontweight='bold')

plt.tight_layout()
plt.show()


# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Calculate Central Tendency
mean_sales = df['Global_Sales'].mean()
median_sales = df['Global_Sales'].median()

print(f"Mean Global Sales: {mean_sales:.2f}M")
print(f"Median Global Sales: {median_sales:.2f}M")

# 2. Visualize the Skew (Boxplot)
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['Global_Sales'], color='skyblue')

# Add lines for Mean and Median to show the gap
plt.axvline(mean_sales, color='red', linestyle='--', label=f'Mean: {mean_sales:.2f}M')
plt.axvline(median_sales, color='green', linestyle='-', label=f'Median: {median_sales:.2f}M')

plt.title('Global Sales Distribution: Spotting the Outliers')
plt.xlabel('Global Sales (Millions)')
plt.legend()
plt.show()

# 3. Identify the "Top 0.1%" (Outliers)
outliers = df[df['Global_Sales'] > df['Global_Sales'].quantile(0.99)]
print(f"Total games in Top 1%: {len(outliers)}")


# In[ ]:




