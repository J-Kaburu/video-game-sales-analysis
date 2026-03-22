```python
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
```

    ===DATA SET SAMPLE===
       Rank                      Name Platform    Year         Genre Publisher  \
    0     1                Wii Sports      Wii  2006.0        Sports  Nintendo   
    1     2         Super Mario Bros.      NES  1985.0      Platform  Nintendo   
    2     3            Mario Kart Wii      Wii  2008.0        Racing  Nintendo   
    3     4         Wii Sports Resort      Wii  2009.0        Sports  Nintendo   
    4     5  Pokemon Red/Pokemon Blue       GB  1996.0  Role-Playing  Nintendo   
    
       NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  
    0     41.49     29.02      3.77         8.46         82.74  
    1     29.08      3.58      6.81         0.77         40.24  
    2     15.85     12.88      3.79         3.31         35.82  
    3     15.75     11.01      3.28         2.96         33.00  
    4     11.27      8.89     10.22         1.00         31.37  
    
    ===DATA SHAPE===
    Dataset Shape: (16598, 11)
    
    ===DATA TYPES===
    Rank              int64
    Name             object
    Platform         object
    Year            float64
    Genre            object
    Publisher        object
    NA_Sales        float64
    EU_Sales        float64
    JP_Sales        float64
    Other_Sales     float64
    Global_Sales    float64
    dtype: object
    


```python
#Check for missing values
print("===== MISSING VALUES PER COLUMN =====")
print(df.isnull().sum())

print("\n===== COLUMNS WITH MISSING VALUES =====")
missing_cols = df.isnull().sum()
print(missing_cols[missing_cols > 0])


```

    ===== MISSING VALUES PER COLUMN =====
    Rank              0
    Name              0
    Platform          0
    Year            271
    Genre             0
    Publisher        58
    NA_Sales          0
    EU_Sales          0
    JP_Sales          0
    Other_Sales       0
    Global_Sales      0
    dtype: int64
    
    ===== COLUMNS WITH MISSING VALUES =====
    Year         271
    Publisher     58
    dtype: int64
    


```python
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
```

    
    ===== COLUMNS WITH MISSING VALUES =====
    Publisher    36
    dtype: int64
    
    ====Convert the Year column to integers====
    ===DATA SET SAMPLE====
       Rank                      Name Platform  Year         Genre Publisher  \
    0     1                Wii Sports      Wii  2006        Sports  Nintendo   
    1     2         Super Mario Bros.      NES  1985      Platform  Nintendo   
    2     3            Mario Kart Wii      Wii  2008        Racing  Nintendo   
    3     4         Wii Sports Resort      Wii  2009        Sports  Nintendo   
    4     5  Pokemon Red/Pokemon Blue       GB  1996  Role-Playing  Nintendo   
    
       NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  
    0     41.49     29.02      3.77         8.46         82.74  
    1     29.08      3.58      6.81         0.77         40.24  
    2     15.85     12.88      3.79         3.31         35.82  
    3     15.75     11.01      3.28         2.96         33.00  
    4     11.27      8.89     10.22         1.00         31.37  
    ===DATA TYPE===
    Rank              int64
    Name             object
    Platform         object
    Year              int64
    Genre            object
    Publisher        object
    NA_Sales        float64
    EU_Sales        float64
    JP_Sales        float64
    Other_Sales     float64
    Global_Sales    float64
    dtype: object
    


```python
regional_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().sum()
print("====TOTAL REGIONAL SALES======")
print (regional_sales)

print("Total Global Sales:", df['Global_Sales'].sum())
print("Total Regional Sales:", df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum().sum())

print ("Difference:", df['Global_Sales'].sum() - df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum().sum())
```

    ====TOTAL REGIONAL SALES======
    8815.86
    Total Global Sales: 8820.360000000002
    Total Regional Sales: 8815.86
    Difference: 4.500000000001819
    


```python
#summary statistics of sales columns
sales_cols = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']

print("=== SUMMARY STATISTICS OF SALES COLUMNS ===")
print(df[sales_cols].describe())
```

    === SUMMARY STATISTICS OF SALES COLUMNS ===
               NA_Sales      EU_Sales      JP_Sales   Other_Sales  Global_Sales
    count  16327.000000  16327.000000  16327.000000  16327.000000  16327.000000
    mean       0.265415      0.147554      0.078661      0.048325      0.540232
    std        0.821591      0.508766      0.311557      0.189885      1.565732
    min        0.000000      0.000000      0.000000      0.000000      0.010000
    25%        0.000000      0.000000      0.000000      0.000000      0.060000
    50%        0.080000      0.020000      0.000000      0.010000      0.170000
    75%        0.240000      0.110000      0.040000      0.040000      0.480000
    max       41.490000     29.020000     10.220000     10.570000     82.740000
    


```python
#Top 10 games by Global_Sales.
print("=== TOP 10 GAMES BY GLOBAL SALES ===")

top10 = df.sort_values(by='Global_Sales', ascending=False).head(10)

print(top10[['Name','Platform','Year','Global_Sales']])
print("\n=== GENRE COUNT IN TOP 10 ===")
print(top10['Genre'].value_counts())

#Top 10 genres?
print("\n=== TOTAL COUNT OF EACH GENRE ===")
print(df['Genre'].value_counts())
```

    === TOP 10 GAMES BY GLOBAL SALES ===
                            Name Platform  Year  Global_Sales
    0                 Wii Sports      Wii  2006         82.74
    1          Super Mario Bros.      NES  1985         40.24
    2             Mario Kart Wii      Wii  2008         35.82
    3          Wii Sports Resort      Wii  2009         33.00
    4   Pokemon Red/Pokemon Blue       GB  1996         31.37
    5                     Tetris       GB  1989         30.26
    6      New Super Mario Bros.       DS  2006         30.01
    7                   Wii Play      Wii  2006         29.02
    8  New Super Mario Bros. Wii      Wii  2009         28.62
    9                  Duck Hunt      NES  1984         28.31
    
    === GENRE COUNT IN TOP 10 ===
    Genre
    Platform        3
    Sports          2
    Racing          1
    Role-Playing    1
    Puzzle          1
    Misc            1
    Shooter         1
    Name: count, dtype: int64
    
    === TOTAL COUNT OF EACH GENRE ===
    Genre
    Action          3253
    Sports          2304
    Misc            1710
    Role-Playing    1471
    Shooter         1282
    Adventure       1276
    Racing          1226
    Platform         876
    Simulation       851
    Fighting         836
    Strategy         671
    Puzzle           571
    Name: count, dtype: int64
    


```python
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
```

    === TOTAL GLOBAL SALES BY GENRE ===
    Genre
    Action          1722.88
    Sports          1309.24
    Shooter         1026.20
    Role-Playing     923.84
    Platform         829.15
    Misc             797.62
    Racing           726.77
    Fighting         444.05
    Simulation       390.16
    Puzzle           242.22
    Adventure        234.80
    Strategy         173.43
    Name: Global_Sales, dtype: float64
    
    === AVERAGE SALES PER GENRE ===
    Genre
    Platform        0.946518
    Shooter         0.800468
    Role-Playing    0.628035
    Racing          0.592798
    Sports          0.568247
    Fighting        0.531160
    Action          0.529628
    Misc            0.466444
    Simulation      0.458472
    Puzzle          0.424203
    Strategy        0.258465
    Adventure       0.184013
    Name: Global_Sales, dtype: float64
    


    
![png](output_6_1.png)
    



    
![png](output_6_2.png)
    



    
![png](output_6_3.png)
    



```python

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
```


    
![png](output_7_0.png)
    



    
![png](output_7_1.png)
    



```python
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
```

                  Total_Sales  Game_Count
    Genre                                
    Action            1722.88        3253
    Adventure          234.80        1276
    Fighting           444.05         836
    Misc               797.62        1710
    Platform           829.15         876
    Puzzle             242.22         571
    Racing             726.77        1226
    Role-Playing       923.84        1471
    Shooter           1026.20        1282
    Simulation         390.16         851
    Sports            1309.24        2304
    Strategy           173.43         671
    

    ERROR: Could not find a version that satisfies the requirement adjust_text (from versions: none)
    ERROR: No matching distribution found for adjust_text
    


    
![png](output_8_2.png)
    



```python
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
```


    
![png](output_9_0.png)
    



```python
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
```


    
![png](output_10_0.png)
    



```python
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
```


    
![png](output_11_0.png)
    



```python
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
```


    
![png](output_12_0.png)
    



```python
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
```

    Mean Global Sales: 0.54M
    Median Global Sales: 0.17M
    


    
![png](output_13_1.png)
    


    Total games in Top 1%: 164
    


```python

```
